<template>
    <div>
    <vue-excel-editor v-model="jsondata" filter-row allow-add-col>
    </vue-excel-editor>
    <vs-button color="#C6D8BB" :active="active == 1" @click="onClick()" style="width: 200px; height: 8vh; display: flex; margin: 1vh auto; ">
        Продолжить
    </vs-button>
    </div> 
</template>

<script>
export default {
    name: 'app',
    data() {
      return {
        jsondata: []
      };
    },
    methods: {
        onClick(){
            console.log(this.jsondata)
        },
        Get(){
            const path = "http://localhost:3000/";
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                this.jsondata = response.data.data;
            })
                .catch((error) => {
            });
        }
    }

}
</script>

<style scoped>
  .vue-excel-editor {
    color: black;
    
  }
</style>