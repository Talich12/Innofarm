import math
from app import app, db, jwt
from flask import jsonify, request, g
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from app.models import User, Garden, Workers, Supplie, RevokedTokenModel, UserSchema, GardenSchema, SupplieSchema
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os
import json

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)



@app.route('/registration', methods=['POST'])
def post_register():
    data = request.get_json()
    login = data['login']
    password = data['password']
    first_name = data['first_name']
    ser_name = data['ser_name']
    last_name = data['last_name']
    date = data['date']
    status = data['status']
    find_user = User.query.filter_by(username=login).count()
    if find_user > 0:
        return jsonify({"status" : "Invalid username"})
    user = User(username=login, first_name = first_name, ser_name = ser_name, last_name = last_name, date = date, status = status)
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

@app.route('/', methods=['GET'])
@jwt_required(refresh=False)
def get_index():
    output = {}
    garden_schema = GardenSchema(many = True)

    username = get_jwt_identity()

    find_user = User.query.filter_by(username = username).first()
    
    if find_user.status == "Admin":
        own_gardens = Garden.query.filter_by(author_id = find_user.id).all()
        own_gardens_json = garden_schema.dump(own_gardens)
        output["own_gardens"] = own_gardens_json


    gardens = Garden.query.join(Workers, (Workers.garden_id == Garden.id)).filter(Workers.worker_id == find_user.id)
    gardens_json = garden_schema.dump(gardens)

    output["gardens"] = gardens_json

    return jsonify(output)


@app.route('/gardenhouse/create', methods=['POST'])
def create_garden():
    data = request.form
    file = request.files['file']
    garden_name = data['garden_name']
    author_username = data['author']

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    find_user = User.query.filter_by(username = author_username).first()
    garden = Garden(name = garden_name, author_id = find_user.id, author = find_user, image = filename)

    db.session.add(garden)
    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/gardenhouse/<id>', methods=['GET'])
def get_garden(id):
    find_garden = Garden.query.filter_by(id = id).first()

    garden_schema = GardenSchema(many = False)
    output = garden_schema.dump(find_garden)

    return jsonify(output)


@app.route('/gardenhouse/<id>/delete', methods=['DELETE'])
def delete_garden(id):
    find_garden = Garden.query.filter_by(id = id).first()

    db.session.delete(find_garden)
    db.session.commit()

    return jsonify({"status": "Success"})



@app.route('/gardenhouse/<id>/add', methods=['POST'])
def add_worker(id):
    data = request.get_json()
    username = data['username']

    find_user = User.query.filter_by(username = username).first()
    find_garden = Garden.query.filter_by(id = id).first()

    worker = Workers(worker_id = find_user.id, worker = find_user, garden_id = find_garden.id, garden = find_garden)

    db.session.add(worker)
    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/gardenhouse/<id>/delete', methods=['POST'])
def delete_worker(id):
    data = request.get_json()
    username = data['username']

    find_user = User.query.filter_by(username = username).first()
    find_garden = Garden.query.filter_by(id = id).first()

    find_worker = Workers.query.filter_by(worker_id = find_user.id, garden_id = find_garden.id).first()

    db.session.delete(find_worker)
    db.session.commit()

    return jsonify({"status": "Success"})


@app.route('/user', methods=['GET'])
@jwt_required(refresh=False)
def user():
    username = get_jwt_identity()
    find_user = User.query.filter_by(username = username).first()

    user_schema = UserSchema(many = False)
    output = user_schema.dump(find_user)

    return jsonify(output)

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


@app.route('/gardenhouse/<id>/table/supplie', methods=['POST'])
def edit_supplie_table(id):
    data = request.get_json()['data']

    find_garden = Garden.query.filter_by(id = id).first()
    find_garden.supplie_table = str(data)

    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/gardenhouse/<id>/table/supplie', methods=['GET'])
def get_supplie_table(id):

    find_garden = Garden.query.filter_by(id = id).first()
    string = find_garden.supplie_table
    string = string.replace("'", "\"")
    json_data = json.loads(string)

    return jsonify(json_data)

@app.route('/gardenhouse/<id>/table/plant', methods=['POST'])
def edit_plant(id):
    data = request.get_json()['data']

    find_garden = Garden.query.filter_by(id = id).first()
    find_garden.plant_table = str(data)

    db.session.commit()

    return jsonify({"status": "Success"})

@app.route('/gardenhouse/<id>/table/plant', methods=['GET'])
def get_plant(id):

    find_garden = Garden.query.filter_by(id = id).first()
    string = find_garden.plant_table
    string = string.replace("'", "\"")
    json_data = json.loads(string)

    return jsonify(json_data)

@app.route('/gardenhouse/<id>/table/finance', methods=['POST'])
def edit_finance(id):
    data = request.get_json()['data']

    supplie = Supplie.query.all()
    supplie_schema = SupplieSchema(many=True)
    supplie_json = supplie_schema.dump(supplie)

    find_garden = Garden.query.filter_by(id = id).first()

    for sup in supplie_json:
        for raw in data:
            if raw['supplie'] == sup['name']:
                raw['cost'] = sup['cost']
                raw['total'] = int(raw['count']) * int(raw['cost'])

    find_garden.finance_table = str(data)
    db.session.commit()

    

    return jsonify({"status": "Success"})

@app.route('/gardenhouse/<id>/table/finance', methods=['GET'])
def get_finance(id):

    find_garden = Garden.query.filter_by(id = id).first()
    string = find_garden.finance_table

    
    string = string.replace("'", "\"")
    json_data = json.loads(string)

    return jsonify(json_data)

@app.route('/supplie', methods=['GET'])
def get_supplie():

    supplie = Supplie.query.all()
    supplie_schema = SupplieSchema(many=True)
    output = supplie_schema.dump(supplie)

    return jsonify(output)


@app.route('/supplie', methods=['POST'])
def add_supplie():
    data = request.get_json()

    name = data['supplie_name']
    cost = data['cost']

    supplie = Supplie(name = name, cost = cost)
    
    db.session.add(supplie)
    db.session.commit()

    return jsonify({'status': 'Success'})


@app.route('/TokenRefresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity = current_user)
    return {'access_token': access_token}

@app.route('/LogoutAccess', methods=['GET'])
@jwt_required(refresh=False)
def logout_access():
    jti = get_jwt()['jti']
    revoked_token = RevokedTokenModel(jti = jti)
    revoked_token.add()
    return jsonify({"msg": "successsss"})

@app.route('/LogoutRefresh', methods=['GET'])
@jwt_required(refresh=True)
def logout_refresh():
    jti = get_jwt()['jti']
    revoked_token = RevokedTokenModel(jti = jti)
    revoked_token.add()
    return jsonify({"msg": "successsss"})