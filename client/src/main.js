import Vue from 'vue'
import App from './App'
import router from './router'

import HeaderProfile from './components/HeaderProfile'
Vue.component('headerprofile', HeaderProfile)

import HeaderMain from './components/HeaderMain'
Vue.component('headermain', HeaderMain)

import GardenhouseCard from './components/GardenhouseCard'
Vue.component('gardenhousecard', GardenhouseCard)

import PatternBackground from './components/PatternBackground'
Vue.component('patternbackground', PatternBackground)

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
