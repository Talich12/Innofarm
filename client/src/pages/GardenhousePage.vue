<template>
    <div class="greenhousepage">
      <buttonback></buttonback>
      <headermain></headermain>
      <div class="button-row">
        <vs-button class="btnsquare"
           color="#999483"
          :active="active == 0"
          :to="$route.path + '/table/supplie'"
        >
        <div class="image-container">
          <img src="../assets/images/clip.svg"/><p>Табель учета расходников</p>
        </div>
        </vs-button>

        <vs-button class="btnsquare"
           color="#999483"
          :active="active == 0"
          @click="active = 0"
        >
        <div class="image-container">
          <img src="../assets/images/calendar.svg"/><p>Календарь культивации</p>
        </div>
        </vs-button>

      </div>
      <div class="button-row">
        <vs-button class="btnsquare"
           color="#999483"
          :active="active == 0"
          @click="active = 0"
          to="/gant"
        >
        <div class="image-container">
          <img src="../assets/images/table.svg"/><p>План-график обслуживания теплицы</p>
        </div>
        </vs-button>

        <vs-button class="btnsquare"
           color="#999483"
          :active="active == 0"
          :to="$route.path + '/table/plant'"
        >
        <div class="image-container">
          <img src="../assets/images/flower.svg"/><p style="font-size: smaller;">Таблица для отслеживания параметров растений</p>
        </div>
        </vs-button>
      </div>
      <div class="button-row">
        <vs-button class="btnsquare"
           color="#999483"
          :active="active == 0"
          :to="$route.path + '/table/finance'"
        >
        <div class="image-container">
          <img src="../assets/images/cash.svg"/><p style="font-size:smaller;">Система финансового учета для отслеживания затрат </p>
        </div>
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
    margin: 0 auto;
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

  .gdbtn {
    width: 15vh;

  }
  </style>
  