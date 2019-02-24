import Vue from 'vue'
import Router from 'vue-router'
// import test from '@/components/Graph'
import test from '../components/ShuffleTest'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Graph',
      component: test
    }
  ]
})
