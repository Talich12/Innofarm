import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueCookies from 'vue-cookies'


import HeaderProfile from './components/HeaderProfile'
Vue.component('headerprofile', HeaderProfile)

import HeaderMain from './components/HeaderMain'
Vue.component('headermain', HeaderMain)

import GardenhouseCard from './components/GardenhouseCard'
Vue.component('gardenhousecard', GardenhouseCard)

import PatternBackground from './components/PatternBackground'
Vue.component('patternbackground', PatternBackground)

import Footer from './components/Footer'
Vue.component('myfooter', Footer)

Vue.config.productionTip = false

axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response.status === 401 || error.response.status === 422){
      console.log("fafdsafasd")
      if ($cookies.isKey("access_token")){
          console.log("fsadflk")
          const path2 ="http://localhost:3000/TokenRefresh";
          axios.get(path2, {headers: {
                      'Authorization': 'Bearer ' + $cookies.get("refresh_token"),
                  }})
          .then((response) => {
              console.log(response.data);
              $cookies.set("access_token", response.data.access_token)
              location.reload()
          })
          .catch((error) => {
              console.log(error);
              router.push('/')
          }); 
      }
      else{
          router.push('/login')
      }
    }
    else{
      console.log('asdf')
      router.push('/login')
    }
  }
);


new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

