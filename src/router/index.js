import Vue from 'vue'
import Router from 'vue-router'
import main from '../components/ElectricityPerCapita'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: main
    }
  ]
})
