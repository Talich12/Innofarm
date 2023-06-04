import Vue from 'vue'
import Vuesax from 'vuesax';
import Router from 'vue-router'
import VueCookies from 'vue-cookies'

import MainPage from '@/pages/MainPage'
import ProfilePage from '@/pages/ProfilePage'
import Gardenhouse from '@/pages/GardenhousePage'
import RegistrationPage from '@/pages/RegistrationPage'
import LoginPage from '@/pages/LoginPage'
import NotificationPage from '@/pages/NotificationPage'

import 'vuesax/dist/vuesax.css';

Vue.use(Router)
Vue.use(Vuesax)
Vue.use(VueCookies)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/profile',
      name: 'ProfilePage',
      component: ProfilePage
    },
    {
      path: '/gardenhouse',
      name: 'Gardenhouse',
      component: Gardenhouse
    },
    {
      path: '/registration',
      name: 'RegistrationPage',
      component: RegistrationPage
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    },
    {
      path: '/notification',
      name: 'Notification',
      component: NotificationPage
    },
  ]
})
