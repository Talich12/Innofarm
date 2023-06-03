import Vue from 'vue'
import App from './App'
import router from './router'

import HeaderProfile from './components/HeaderProfile'
Vue.component('headerprofile', HeaderProfile)

import GardenhouseCard from './components/GardenhouseCard'
Vue.component('gardenhousecard', GardenhouseCard)

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
