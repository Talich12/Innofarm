<template>
    <div>
    <vue-excel-editor v-model="jsondata" filter-row allow-add-col>
        <vue-excel-column field="date" label="Дата" type="date" width="100px" />
        <vue-excel-column field="supplie" label="Рассходник" type="string" width="150px" />
        <vue-excel-column field="mesure" label="Ед. изм." type="string" width="50px" />
        <vue-excel-column field="count" label="Кол-во" type="number" width="75px" />
    </vue-excel-editor>
    <vs-button color="#C6D8BB" @click="active = !active" style="width: 200px; height: 8vh; display: flex; margin: 1vh auto; ">
        Добавить запись
    </vs-button>
    <vs-button color="#C6D8BB" @click="Get()" style="width: 200px; height: 8vh; display: flex; margin: 1vh auto; ">
        Продолжить
    </vs-button>
    <vs-dialog v-model="active">
        <template #header>
          <h4 class="not-margin">
            Создать запись
          </h4>
        </template>


        <div class="con-form">
            <vs-input type="date" v-model="date" placeholder="Выберите дату">
 
            <template #icon>
              #
            </template>
          </vs-input>
          <vs-input v-model="supplie" placeholder="Введите расходник">
            <template v-if="error1" #message-danger >
                        Поле пусто
                    </template>
            <template #icon>
              #
            </template>
          </vs-input>
          <vs-input v-model="mesure" placeholder="Введите ед. изм.">
            <template v-if="error2" #message-danger >
                        Поле пусто
                    </template>
            <template #icon>
              #
            </template>
          </vs-input>
          <vs-input v-model="count" placeholder="Введите кол-во">
            <template v-if="error3" #message-danger >
                        Не может быть 0 или меньше
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
    </div> 
</template>

<script>
import axios from 'axios';
export default {
    name: 'app',
    data() {
      return {
        date: '',
        active: false,
        supplie: '',
        mesure: '',
        error1: true,
        error2: true,
        error3: true,
        count: 0,
        jsondata: [
        ]
      };
    },
    methods: {
        onClick(){
            console.log(this.jsondata)
        },
        Get(){
            const path = "http://localhost:3000/garden/2/table/supplie";
            axios.get(path)
                .then((response) => {
                console.log(response.data);
                this.jsondata = response.data
            })
                .catch((error) => {
            });
        },
        onClick(){
            if (this.error1 || this.error2 || this.error3){
                return
            }
            this.active = !this.active
            const data = {date: this.date, supplie: this.supplie, mesure: this.mesure, count: this.count}
            this.jsondata.push(data)
            console.log(this.jsondata)
            const path = "http://localhost:3000/garden/2/table/supplie";
            axios.post(path, {data: this.jsondata})
                .then((response) => {
                console.log(response.data);
                this.jsondata = response.data
            })
                .catch((error) => {
            });
        }

    },
    created(){
        this.Get()
    },
    watch:{
        supplie: function(){
            if (this.supplie === ""){
                this.error1 = true
            }
            else{
                this.error1 = false
            }
        },
        mesure: function(){
            if (this.mesure === ""){
                this.error2 = true
            }
            else{
                this.error2 = false
            }
        },
        count: function(){
            if (this.count <= 0){
                this.error3 = true
            }
            else{
                this.error3 = false
            }
        }
    }

}
</script>

<style scoped>
  .vue-excel-editor {
    color: black;
    
  }
</style>