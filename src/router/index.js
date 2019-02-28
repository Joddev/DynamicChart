import Vue from 'vue'
import Router from 'vue-router'
// import lifeExpectancy from '../components/LifeExpectancy.vue'
// import urbanPopulation from '../components/UrbanPopulation'
import co2Emission from '../components/Co2Emission'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'life-expectancy',
    //   component: lifeExpectancy
    // },
    // {
    //   path: '/',
    //   name: 'urban-population',
    //   component: urbanPopulation
    // },
    {
      path: '/',
      name: 'co2-emission',
      component: co2Emission
    }
  ]
})
