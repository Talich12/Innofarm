<template>
    <div class="greenhousepage">
    <patternbackground></patternbackground>
      <div class="button-row">
        <vs-button
           color="#776F66"
          :active="active == 0"
          @click="active = 0"
        >
          Active
        </vs-button>
        <vs-button
           color="#776F66"
          :active="active == 0"
          @click="active = 0"
        >
          Active
        </vs-button>
      </div>
      <div class="button-row">
        <vs-button
           color="#776F66"
          :active="active == 0"
          @click="active = 0"
        >
          Active
        </vs-button>
        <vs-button
           color="#776F66"
          :active="active == 0"
          @click="active = 0"
        >
          Active
        </vs-button>
      </div>
      <div class="button-row">
        <vs-button
           color="#776F66"
          :active="active == 0"
          @click="active = 0"
        >
          Active
        </vs-button>
        <vs-button
           color="#776F66"
          :active="active == 0"
          @click="active = 0"
        >
          Active
        </vs-button>
      </div>
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
  