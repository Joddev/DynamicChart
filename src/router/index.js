import Vue from 'vue'
import Router from 'vue-router'
import main from '../components/Aged'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: main
    }
  ]
})
