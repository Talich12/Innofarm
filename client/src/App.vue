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
</style>