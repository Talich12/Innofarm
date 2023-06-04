<template>
    <div class="center content-inputs" style="margin-top: 12vh;">
        <vs-input v-model="login" placeholder="Login" style="width: 200px; display: block; margin: 1vh auto;"/>
        <vs-input v-model="password" placeholder="Password" style="width: 200px; display: block; margin: 1vh auto;"/>

        <vs-button color="#C6D8BB" :active="active == 1" @click="onClick()" style="width: 200px; height: 8vh; display: flex; margin: 1vh auto; ">
            Продолжить
        </vs-button>
    </div>
</template>

<script>
import axios from 'axios';

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
            })
            .catch((error) => {
                console.log(error);
            }); 
        }
    }
    
}
</script>

        