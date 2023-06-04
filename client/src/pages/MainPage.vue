<template>
    <div class="main-container">
        <headerprofile :name="this.name"/>
        <patternbackground></patternbackground>
        <h3 v-if="this.User.gardens" style="margin-top: 3vh; z-index: 5; font-weight: bolder;">Теплицы в которых вы работаете:</h3>
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
        <h3 v-if="this.User.own_gardens" style="z-index: 5; font-weight: bolder;" >Теплицы в которых вы админ:</h3>
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
            v-if="this.User.status === 'Admin'"
            @click="active = !active"
            block
            color="#C6D8BB"
            style="max-width: 300px; height: 25vh; margin: 5vh auto; box-shadow: 0px 7px 12px rgba(0, 0, 0, 0.35); border-radius: 25px;"
        >
            <i class='bx bxs-paint-roll' ></i> Добавить новую теплицу
        </vs-button>
        <vs-dialog v-model="active">
        <template #header>
          <h4 class="not-margin">
            Создать теплицу
          </h4>
        </template>


        <div class="con-form">
          <vs-input v-model="garden_name" placeholder="Введите название">
            <template v-if="error" #message-danger >
                        Поле пусто
                    </template>
            <template #icon>
              #
            </template>
          </vs-input>
        </div>

        <template #footer>
          <div class="footer-dialog">
            <vs-button @click="onClick()" block>
              Добавить теплицу
            </vs-button>
          </div>
        </template>
      </vs-dialog>
        <myfooter></myfooter>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "index",
  data() {
      return {
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
        const path = "http://localhost:3000/garden/create"
        axios.post(path, {garden_name: this.garden_name, author: this.User.username}, {headers: {
                'Authorization': 'Bearer ' + this.$cookies.get("access_token"),
            }})
            .then((response) => {
            console.log(response.data);
            this.Get()
            this.active = !this.active
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