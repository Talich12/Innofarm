<template>
    <div class="greenhousepage">
      <headermain></headermain>
      <div class="button-row">
        <vs-button
           color="#999483"
          :active="active == 0"
          :to="$route.path + '/table/supplie'"
        >
          Табель учета расходников
        </vs-button>
        <vs-button
           color="#999483"
          :active="active == 0"
          @click="active = 0"
        >
          Календарь культивации
        </vs-button>
      </div>
      <div class="button-row">
        <vs-button
           color="#999483"
          :active="active == 0"
          @click="active = 0"
        >
        <div class="image-container">
          <img src="../assets/images/table2.svg"/><p>План-график обслуживания теплицы</p>
        </div>
        </vs-button>
        <vs-button
           color="#999483"
          :active="active == 0"
          @click="active = 0"
        >
          Таблица для отслеживания параметров растений
        </vs-button>
      </div>
      <div class="button-row">
        <vs-button
           color="#999483"
          :active="active == 0"
          @click="active = 0"
        >
          Система финансового учета для отслеживания затрат 
        </vs-button>
        <vs-button
           color="#999483"
          :active="active == 0"
          @click="active = 0"
        >
          Система оповещения
        </vs-button>
      </div>
      <myfooter></myfooter>
    </div>
  </template>
  
  <script>
  export default {
    data: () => ({
      active: 0
    })
  };
  </script>
  
  <style>
  .image-container img {
    max-width: 50%;
    margin: auto;
  }

  .greenhousepage {
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  .button-row {
    display: flex;
    justify-content: space-between;
    padding: 4vh;
  }
  </style>
  