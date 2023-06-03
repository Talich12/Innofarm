import Vue from 'vue'
import Vuesax from 'vuesax';
import Router from 'vue-router'

import MainPage from '@/pages/MainPage'

import 'vuesax/dist/vuesax.css';

Vue.use(Router)
Vue.use(Vuesax)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    }
  ]
})
