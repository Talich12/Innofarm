<template>
    <div class="main-container">
        <headerprofile />
        <h3 v-if="Data.gardens">Теплицы в которых вы работаете</h3>
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
        <h3 v-if="Data.own_gardens">Теплицы в которых вы админ</h3>
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
          axios.post(path, {username: "Denis"})
              .then((response) => {
              console.log(response.data.gardens);
              this.Data = response.data;
          })
              .catch((error) => {
              console.log(error);
          });
      },
  },
  created() {
    this.Get()
  },
};
</script>