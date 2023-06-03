<template>
    <div class="center content-inputs">
        <vs-input v-model="login" placeholder="Login" />
        <vs-input v-model="password" placeholder="Password" />
        <vs-input v-model="repeat_password" placeholder="Repeat password" />

        <vs-button :active="active == 1" @click="onClick()">
            Commit
        </vs-button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data:() => ({
    login: '',
    password: '',
    repeat_password: '',
    active: 0,
    }),
    methods:{
        onClick(){
            const path = "http://localhost:3000/registration";
            if (this.password == this.repeat_password){
                axios.post(path, {login: this.login, password: this.password, status: "worker"})
                .then((response) => {
                    console.log(response.data);
                })
                .catch((error) => {
                    console.log(error);
                }); 
            }
        }
    }
    
}
</script>

        