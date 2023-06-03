<template>
  <div id="app">
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
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  height: 100vh;
  background-color: #B7C6AE;
}

.vs-avatar img {
  height: 100%;
}

.vs-card {
  margin: 0 auto;
}

.vs-card__img {
  height: 25vh;
}
</style>