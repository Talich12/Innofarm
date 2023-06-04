<template>
    <div>
        <buttonback></buttonback>
    <vue-excel-editor v-model="jsondata" height="1120" no-paging no-footer filter-row allow-add-col>
        <vue-excel-column field="date" label="Дата" type="date"  />
        <vue-excel-column field="supplie" label="Рассходник" type="string" :options="this.supplie" width="188px" />
        <vue-excel-column field="count" label="Кол-во" type="number" />
    </vue-excel-editor>
    <div style="display: flex;">
        <vs-button 
            color="#C6D8BB" @click="onClick()" style="width: 46%; height: 8vh; display: flex; margin: 2vh auto; ">
            Добавить запись
        </vs-button>
        <vs-button color="#C6D8BB" @click="Post()" style="width: 46%; height: 8vh; display: flex; margin: 2vh auto; ">
            Сохранить
        </vs-button>
    </div>
    <vs-button color="#C6D8BB" @click="active = !active" style="width: 46%; height: 8vh; display: flex; margin: 2vh auto; ">
        Добавить расходник
    </vs-button>

    <vs-dialog v-model="active">
        <template #header>
          <h4 class="not-margin">
            Создать расходник
          </h4>
        </template>


        <div class="con-form">
          <vs-input v-model="supplie_name" placeholder="Введите название" style="width: 100%;">
           
          </vs-input>
          <vs-input v-model="cost" placeholder="Введите стоимость" style="width: 100%;">
            
          </vs-input>
        </div>

        <template #footer>
          <div class="footer-dialog">
            <vs-button @click="AddSupplie()" block>
              <p>Добавить теплицу</p>
            </vs-button>
          </div>
        </template>
      </vs-dialog>
    </div> 
</template>

<script>
import axios from 'axios';
export default {
    name: 'app',
    data() {
      return {
        supplie_name: '',
        cost: '',
        active: false,
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

            const path2 = "http://localhost:3000/gardenhouse/" + this.$route.params.id + "/table/finance";
            axios.post(path2, {data: this.jsondata})
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
        },
        AddSupplie(){
            const path = "http://localhost:3000/supplie"

            axios.post(path, {supplie_name: this.supplie_name, cost: this.cost})
                .then((response) => {
                    console.log(response.data)
                    this.$router.go(0)
            })
                .catch((error) => {
            });
        }

    },
    created(){
        this.Get()
        this.GetSupplie()
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