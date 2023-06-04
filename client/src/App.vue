<template>
  <div id="app">
    <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&family=Montserrat&display=swap" rel="stylesheet"> 
    <Header />
    <router-view/>
  </div>
</template>

<script>
import HeaderProfile from './components/HeaderProfile.vue';

export default {
    name: "App",
}
</script>

<style>
@import 'assets/css/reset.css';

#app {
  font-family: "Montserrat", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  height: 100%;
  background-color: #B7C6AE;
  overflow-y:visible;
  scrollbar-color: rgb(55, 97, 57) rgb(55, 97, 57);
}

body {
  background-color: #B7C6AE;
}

.vs-avatar img {
  height: 100%;
}

.vs-card {
  margin: 5vh auto;
}

.vs-card__img {
  height: 25vh;
}

.vs-card__text {
  width: 100%;
}

.vs-button__content {
        height: 15vh;
        width: 15vh;
}
.vs-card-content.type-4 .vs-card__text {
  background-color: #C6D8BB;
}
.vs-input {
  background-color: #C6D8BB;
  box-shadow: 0px 4px 7px rgba(0, 0, 0, 0.35);
}
.vs-input-content {
  color: black;
  opacity: 1;
}
.vs-select__input {
  background: #C6D8BB;
  box-shadow: 0px 4px 7px rgba(0, 0, 0, 0.35);
  color: #76816f;
}
.vs-button {
  color: #76816f;
  box-shadow: 0px 4px 7px rgba(0, 0, 0, 0.35); 
}
p {
  font-family: "Montserrat", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.systable th[data-v-cf2e49d2]:not() {
    background: #DFE9D9;
  }
.systable tbody tr td[data-v-cf2e49d2]{
  background: #B4B9B1;
  }
  .vs-input {
    color: #76816f;
  }

</style>