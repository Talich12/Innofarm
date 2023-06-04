import Vue from 'vue'
import Vuesax from 'vuesax';
import Router from 'vue-router'
import VueCookies from 'vue-cookies'
import VueExcelEditor from 'vue-excel-editor'

import MainPage from '@/pages/MainPage'
import ProfilePage from '@/pages/ProfilePage'
import Gardenhouse from '@/pages/GardenhousePage'
import RegistrationPage from '@/pages/RegistrationPage'
import LoginPage from '@/pages/LoginPage'
import NotificationPage from '@/pages/NotificationPage'
import SupplieTable from '@/pages/SupplieTable'
import PlantTable from '@/pages/PlantTable'
import FinanceTable from '@/pages/FinanceTable'
import Gant from '@/pages/Gant'

import 'vuesax/dist/vuesax.css';

Vue.use(Router)
Vue.use(Vuesax)
Vue.use(VueCookies)
Vue.use(VueExcelEditor)

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
      path: '/gardenhouse/:id',
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
    {
      path: '/gardenhouse/:id/table/supplie',
      name: 'SupplieTable',
      component: SupplieTable
    },
    {
      path: '/gardenhouse/:id/table/plant',
      name: 'PlantTable',
      component: PlantTable
    },
    {
      path: '/gardenhouse/:id/table/finance',
      name: 'FinanceTable',
      component: FinanceTable
    },
    {
      path: '/gant',
      name: 'Gant',
      component: Gant
    },
  ]
})
