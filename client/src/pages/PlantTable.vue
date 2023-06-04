<template>
    <div>
        <buttonback></buttonback>
    <vue-excel-editor v-model="jsondata"  filter-row allow-add-col>
        <vue-excel-column field="date" label="Дата" type="date" width="100px" />
        <vue-excel-column field="henobase" label="Фенофаза" type="string"  />
        <vue-excel-column field="height" label="Средняя высота растений, см" type="string"  />
        <vue-excel-column field="leaves" label="Среднее кол-во листьев, шт" type="number"  />
        <vue-excel-column field="height2" label="Средняя высота, см" type="number"  />
        <vue-excel-column field="leaves2" label="Среднее количество междоузлий, см" type="number" />
        <vue-excel-column field="weight" label="Средняя масса после снятия, г" type="number"  />
        <vue-excel-column field="square" label="Средняя площадь поверхности листьев" type="number"  />
        <vue-excel-column field="notes" label="Примечания" type="string"  />
    </vue-excel-editor>
    <vs-button color="#C6D8BB" @click="onClick()" style="width: 200px; height: 8vh; display: flex; margin: 1vh auto; ">
        Добавить запись
    </vs-button>
    <vs-button color="#C6D8BB" @click="Post()" style="width: 200px; height: 8vh; display: flex; margin: 1vh auto; ">
        Сохранить
    </vs-button>
    </div> 
</template>

<script>
import axios from 'axios';
export default {
    name: 'app',
    data() {
      return {
        jsondata: [
        ]
      };
    },
    methods: {
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