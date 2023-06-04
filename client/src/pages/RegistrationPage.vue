<template>
    <div  class="center content-inputs">
        Логин
        <vs-input v-model="login" placeholder="Login" />
        Пароль
        <vs-input v-model="password" placeholder="Password" />
        Повторите паоль
        <vs-input v-model="repeat_password" placeholder="Repeat password" />
        Имя
        <vs-input v-model="first_name" placeholder="Имя" />
        Фамилия
        <vs-input v-model="ser_name" placeholder="Фамилия" />
        Отчество
        <vs-input v-model="last_name" placeholder="Отчество" />
        Дата рождения
        <vs-input type="date" v-model="date" label="Date"/>

        <vs-select placeholder="Select" v-model="status">
            <vs-option label="Admin" value="Admin">
            Admin
            </vs-option>
            <vs-option label="Worker" value="Worker">
            Worker
            </vs-option>
        </vs-select>

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

        