<template>
    <div>
        <buttonback></buttonback>
    <vue-excel-editor v-model="jsondata" height="1120" no-paging no-footer filter-row allow-add-col>
        <vue-excel-column field="date" label="Дата" type="date"  />
        <vue-excel-column field="supplie" label="Рассходник" type="string" :options="this.supplie"  />
        <vue-excel-column field="count" label="Кол-во" type="number" />
        <vue-excel-column field="cost" label="Стоимость" type="string"/>
        <vue-excel-column field="total" label="Итого" type="string" summary="sum"/>
    </vue-excel-editor>
    </div> 
</template>

<script>
import axios from 'axios';
export default {
    name: 'app',
    data() {
      return {
        jsondata: [],
        supplie: [],
      };
    },
    methods: {
        onClick(){
            console.log(this.jsondata)
        },
        Get(){
            const path = "http://localhost:3000" + this.$route.path;
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                this.jsondata = response.data
            })
                .catch((error) => {
            });
        },
        Post(){
            const path = "http://localhost:3000" + this.$route.path;

            axios.post(path, {data: this.jsondata})
                .then((response) => {
                console.log(response.data);
            })
                .catch((error) => {
            });
        },
        onClick(){
            const data = {}
            this.jsondata.push(data)
            console.log(this.jsondata)
        },
        GetSupplie(){
            const path = "http://localhost:3000/supplie"

            axios.get(path)
                .then((response) => {
                    console.log(response.data)
                    var data = response.data
                    for (var sup in data){
                        this.supplie.push(data[sup].name)
                    }
                    console.log(this.supplie)
            })
                .catch((error) => {
            });
        }

    },
    created(){
        this.Get()
    },
}
</script>

<style scoped>
  .vue-excel-editor {
    color: black;
    
  }
  .vs-button {
    background-color: #C6D8BB;
  }
</style>