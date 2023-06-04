<template>
    <div class="center content-inputs">
        <vs-input v-model="login" placeholder="Login" />
        <vs-input v-model="password" placeholder="Password" />

        <vs-button :active="active == 1" @click="onClick()">
            Commit
        </vs-button>
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

        