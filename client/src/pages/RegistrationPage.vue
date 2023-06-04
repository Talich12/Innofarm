<template>
    <div>
        <patternbackground></patternbackground>
    <div  class="center content-inputs" style="margin-top: 12vh;">
        Логин
        <vs-input v-model="login" placeholder="Login" style="width: 200px; display: block; margin: 1vh auto;"/>
        Пароль
        <vs-input v-model="password" placeholder="Password" style="width: 200px; display: block; margin: 1vh auto;"/>
        Повторите паоль
        <vs-input v-model="repeat_password" placeholder="Repeat password" style="width: 200px; display: block; margin: 1vh auto;"/>
        Имя
        <vs-input v-model="first_name" placeholder="Имя" style="width: 200px; display: block; margin: 1vh auto;"/>
        Фамилия
        <vs-input v-model="ser_name" placeholder="Фамилия" style="width: 200px; display: block; margin: 1vh auto;"/>
        Отчество
        <vs-input v-model="last_name" placeholder="Отчество" style="width: 200px; display: block; margin: 1vh auto;"/>
        Дата рождения
        <vs-input type="date" v-model="date" style="width: 200px; display: block; margin: 1vh auto;"/>

        <vs-select color="#C6D8BB" placeholder="Select" v-model="status" style="width: 200px; display: block; margin: 3vh auto;">
            <vs-option label="Admin" value="Admin">
            Admin
            </vs-option>
            <vs-option label="Worker" value="Worker">
            Worker
            </vs-option>
        </vs-select>

        <vs-button color="#C6D8BB" :active="active == 1" @click="onClick()" style="width: 200px; height: 8vh; display: flex; margin: 1vh auto; ">
            <p>Продолжить</p>
        </vs-button>
    </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data:() => ({
    login: '',
    password: '',
    repeat_password: '',
    first_name: '',
    ser_name: '',
    last_name: '',
    date: '',
    status: '',
    active: 0,
    }),
    methods:{
        onClick(){
            const path = "http://localhost:3000/registration";
            if (this.password == this.repeat_password){
                axios.post(path, {login: this.login, password: this.password, first_name: this.first_name, ser_name: this.ser_name, last_name: this.last_name, date: this.date, status: this.status })
                .then((response) => {
                    console.log(response.data);
                })
                .catch((error) => {
                    console.log(error);
                }); 
            }
        }
    },
    watch:{
        date: function(){
            console.log(this.date)
        }
    }
    
}
</script>

<style scoped>

</style>