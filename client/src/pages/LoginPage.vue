<template>
    <div class="dkaksd">
    <div class="content-inputs" style="margin-top: 12vh;">
        <div class="image-container">
          <img src="../assets/images/logo.png">
        </div>
        <vs-input v-model="login" placeholder="Логин" style="width: 200px; display: block; margin: 2vh auto;"/>
        <vs-input v-model="password" placeholder="Пароль" style="width: 200px; display: block; margin: 2vh auto;"/>

        <vs-button color="#C6D8BB" :active="active == 1" @click="onClick()" style="width: 200px; height: 8vh; display: flex; margin: 2vh auto; ">
            Продолжить
        </vs-button>
    </div>
    </div>
</template>

<script>
import axios from 'axios';
import router from '../router';

export default {
    data:() => ({
    login: '',
    password: '',
    active: 0,
    }),
    methods:{
        onClick(){
            const path = "http://localhost:3000/login";
            axios.post(path, {login: this.login, password: this.password})
            .then((response) => {
                console.log(response.data);
                this.$cookies.set("access_token", response.data.access_token)
                this.$cookies.set("refresh_token", response.data.refresh_token)
                console.log($cookies.get("access_token"))
                router.push('/')
            })
            .catch((error) => {
                console.log(error);
            }); 
        }
    }
    
}
</script>

<style>
.content-inputs {
    z-index: 10;
}
.image-container img {
    max-width: 100%;
    height: 6vh;
    margin: 0 auto;
  }
</style>