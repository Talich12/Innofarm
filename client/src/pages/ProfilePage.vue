<template>
    <div class="profilecontainer">
        <buttonback></buttonback>
        <patternbackground></patternbackground>
        <headerprofile :name="this.name"/>
        <p style="background-color: aliceblue; width: 50vw; height: 2.5vh; color: #76816f; border-radius: 15px; display: flex; margin: 2vh auto; justify-content: center;">Должность</p>
        <p>djdjjdj</p>
        <p style="background-color: aliceblue; width: 80vw; height: 2.5vh; color: #76816f; border-radius: 15px; display: flex; margin: 2vh auto; justify-content: center;">Персональная информация</p>
        <p>ddd</p>
        <p style="background-color: aliceblue; width: 50vw; height: 2.5vh; color: #76816f; border-radius: 15px; display: flex; margin: 2vh auto; justify-content: center;">Пропуск</p>
        <div class="qr-container">
          <img src="../assets/images/qr.png" style="height: 300px;">
        </div>
        <myfooter></myfooter>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "index",
  data() {
      return {
        file: null,
        error: true,
        garden_name: '',
        active: false,
        Data: [],
        User: [],
        name: ''
      };
  },
  methods: {
      Get() {
        const path = "http://localhost:3000/";
        axios.get(path, {headers: {
                'Authorization': 'Bearer ' + this.$cookies.get("access_token"),
            }})
            .then((response) => {
            console.log(response.data);
            this.Data = response.data;
        })
            .catch((error) => {
        });
      },
      GetUser(){
        const path = "http://localhost:3000/user";
        axios.get(path, {headers: {
                'Authorization': 'Bearer ' + this.$cookies.get("access_token"),
            }})
            .then((response) => {
            console.log(response.data);
            this.User = response.data;
            this.name = response.data.ser_name + ' ' + response.data.first_name + ' ' + response.data.last_name
        })
            .catch((error) => {
                console.log(error.response.status);
        });
      },
      onClick(){
        if (this.error){
            return
        }
        const fd = new FormData();
        fd.append('garden_name', this.garden_name)
        fd.append('file', this.file)
        fd.append('author', this.User.username)
        console.log(fd)
        const path = "http://localhost:3000/gardenhouse/create"
        axios.post(path, fd)
            .then((response) => {
            console.log(response.data);
            this.Get()
            this.active = !this.active
        })
            .catch((error) => {
                console.log(error.response.status);
        });
      },
      OnFileSelected(event) {
        this.file = event.target.files[0]
        console.log(event)
      },
  },
  created() {
    this.Get()
    this.GetUser()
  },
  watch: {
    garden_name: function(){
        if (this.garden_name == ''){
            this.error = true
        }
        else{
            this.error = false
        }
    }
  }
};
</script>

<style scoped>
    .qr-container {
        width: 100%;
        margin: 0 auto;
    }
</style>