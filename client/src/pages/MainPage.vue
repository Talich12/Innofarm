<template>
    <div class="main-container">
        <headerprofile :name="this.User.username"/>
        <patternbackground></patternbackground>
        <h3 style="z-index: 5; font-weight: bolder; position: relative; margin: 3vh auto;">Теплицы в которых вы работаете:</h3>
        <div v-for="garden in Data.gardens" class="gardenhouse">
            <gardenhousecard>
                <template #title>
                    {{ garden.name}}
                </template>
                <template #text>
                    asdfsadfsdfsa
                </template>
            </gardenhousecard>
        </div>
        
        <div v-for="garden in Data.own_gardens" class="gardenhouse">
            <gardenhousecard>
                <template #title>
                    {{ garden.name}}
                </template>
                <template #text>
                    asdfsadfsdfsa
                </template>
            </gardenhousecard>
        </div> 
        <vs-button
            block
            color="#B7C6AE"
            style="max-width: 300px; height: 25vh; margin: 5vh auto; box-shadow: 0px 7px 12px rgba(0, 0, 0, 0.35); border-radius: 25px;"
        >
            <i class='bx bxs-paint-roll' ></i> Добавить новую теплицу
        </vs-button>
        <myfooter></myfooter>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "index",
  data() {
      return {
        Data: [],
        User: [],
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
        })
            .catch((error) => {
                console.log(error.response.status);
        });
      }
  },
  created() {
    this.Get()
    this.GetUser()
  },
};
</script>