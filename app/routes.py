import math
from app import app, db, jwt
from flask import jsonify, request, g
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from app.models import User, Garden, Workers, Supplie, Metric, RevokedTokenModel, UserSchema, GardenSchema, SupplieSchema, MetricSchema
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/registration', methods=['POST'])
def post_register():
    data = request.get_json()
    login = data['login']
    password = data['password']
    status = data['status']
    find_user = User.query.filter_by(username=login).count()
    if find_user > 0:
        return jsonify({"status" : "Invalid username"})
    user = User(username=login, status = status)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"status" : "Success"})

@app.route('/login', methods=['POST'])
def post_login():
    data = request.get_json()
    login = data['login']
    password = data['password']
    find_user = User.query.filter_by(username=login).first()
    if find_user is None or not find_user.check_password(password):
        return jsonify({"status" : "Invalid username or password"})
    access_token = create_access_token(identity = login)
    refresh_token = create_refresh_token(identity = login)

    return jsonify({
        "status" : "Success",   
        "access_token" : access_token,
        "refresh_token" : refresh_token
        })

@app.route('/', methods=['POST'])
def get_index():
    output = {}
    garden_schema = GardenSchema(many = True)

    data = request.get_json()
    username = data['username']

    find_user = User.query.filter_by(username = username).first()
    
    if find_user.status == "admin":
        own_gardens = Garden.query.filter_by(author_id = find_user.id).all()
        own_gardens_json = garden_schema.dump(own_gardens)
        output["own_gardens"] = own_gardens_json


    gardens = Garden.query.join(Workers, (Workers.garden_id == Garden.id)).filter(Workers.worker_id == find_user.id)
    gardens_json = garden_schema.dump(gardens)

    output["gardens"] = gardens_json

    return jsonify(output)



@app.route('/garden/create', methods=['POST'])
def create_garden():
    data = request.get_json()
    garden_name = data['garden_name']
    author_username = data['author']

    find_user = User.query.filter_by(username = author_username).first()
    garden = Garden(name = garden_name, author_id = find_user.id, author = find_user)

    db.session.add(garden)
    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/garden/<id>', methods=['GET'])
def get_garden(id):
    find_garden = Garden.query.filter_by(id = id).first()

    garden_schema = GardenSchema(many = False)
    output = garden_schema.dump(find_garden)

    return jsonify(output)

@app.route('/garden/<id>/metric', methods=['GET'])
def get_metric(id):
    find_garden = Garden.query.filter_by(id = id).first()

    find_metric = Metric.query.filter_by(garden_id = find_garden.id).all()

    metric_schema = MetricSchema(many = True)
    output = metric_schema.dump(find_metric)

    return jsonify(output)


@app.route('/garden/<id>/metric/add', methods=['POST'])
def add_metric(id):
    data = request.get_json()
    name = data["name"]
    count = data["count"]

    find_supplie = Supplie.query.filter_by(name = name).first()
    find_garden = Garden.query.filter_by(id = id).first()

    metric = Metric(supplie_id = find_supplie.id, supplie = find_supplie, garden_id = find_garden.id, garden = find_garden, count = count)

    db.session.add(metric)
    db.session.commit()

    return jsonify({"status" : "Success"})

@app.route('/garden/<id>/metric/<metric_id>/delete', methods=['DELETE'])
def delete_metric(id, metric_id):
    
    find_metric = Metric.query.filter_by(id = metric_id).first()

    db.session.delete(find_metric)
    db.session.commit()

    return jsonify({"status" : "Success"})

@app.route('/garden/<id>/delete', methods=['DELETE'])
def delete_garden(id):
    find_garden = Garden.query.filter_by(id = id).first()

    db.session.delete(find_garden)
    db.session.commit()

    return jsonify({"status": "Success"})



@app.route('/garden/<id>/add', methods=['POST'])
def add_worker(id):
    data = request.get_json()
    username = data['username']

    find_user = User.query.filter_by(username = username).first()
    find_garden = Garden.query.filter_by(id = id).first()

    worker = Workers(worker_id = find_user.id, worker = find_user, garden_id = find_garden.id, garden = find_garden)

    db.session.add(worker)
    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/garden/<id>/delete', methods=['POST'])
def delete_worker(id):
    data = request.get_json()
    username = data['username']

    find_user = User.query.filter_by(username = username).first()
    find_garden = Garden.query.filter_by(id = id).first()

    find_worker = Workers.query.filter_by(worker_id = find_user.id, garden_id = find_garden.id).first()

    db.session.delete(find_worker)
    db.session.commit()

    return jsonify({"status": "Success"})


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    find_user = User.query.filter_by(id = id).first()

    user_schema = UserSchema(many = False)
    output = user_schema.dump(find_user)

    return jsonify(output)

@app.route('/user/<id>/delete', methods=['DELETE'])
def delete_user(id):
    find_user = User.query.filter_by(id = id).first()

    db.session.delete(find_user)
    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/supplie', methods=['GET'])
def get_supplie():
    find_supplie = Supplie.query.all()
    
    supplie_schema = SupplieSchema(many = True)

    output = supplie_schema.dump(find_supplie)

    return jsonify(output)

@app.route('/supplie/add', methods=['POST'])
def add_supplie():
    data = request.get_json()
    
    name = data['name']
    measure = data['mesure']

    supplie = Supplie(name = name, measure = measure)

    db.session.add(supplie)
    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/supplie/<id>/delete', methods=['DELETE'])
def delete_supplie(id):
    find_supplie = Supplie.query.filter_by(id = id).first()

    db.session.delete(find_supplie)
    db.session.commit()

    return jsonify({"status": "Success"})
