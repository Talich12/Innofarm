<template>
    <div class="main-container">
        <headerprofile />
        <patternbackground></patternbackground>
        <h3 style="margin-top: 3vh; z-index: 5; font-weight: bolder;" v-if="Data.gardens != []">Теплицы в которых вы работаете:</h3>
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
        <h3 style="z-index: 5; font-weight: bolder;" v-if="Data.own_gardens">Теплицы в которых вы админ:</h3>
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
                if (error.response.status === 401){
                    if (this.$cookies.isKey("access_token")){

                        const path2 ="http://localhost:3000/TokenRefresh";
                        axios.get(path, {headers: {
                                    'Authorization': 'Bearer ' + this.$cookies.get("access_token"),
                                }})
                        .then((response) => {
                            console.log(response.data);
                            this.$cookies.set("access_token", response.data.access_token)
                        })
                        .catch((error) => {
                            console.log(error);
                            this.$route.push('/login')
                        }); 
                    }
                    else{
                        this.$route.push('/login')
                    }
                }
                console.log(error.response.status);
          });
      },
  },
  created() {
    this.Get()
  },
};
</script>