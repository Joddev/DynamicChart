import Vue from 'vue'
import Router from 'vue-router'
import lifeExpectancy from '../components/LifeExpectancy.vue'
import urbanPopulation from '../components/UrbanPopulation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/A',
      name: 'life-expectancy',
      component: lifeExpectancy
    },
    {
      path: '/',
      name: 'urban-population',
      component: urbanPopulation
    }
  ]
})
