<template>
  <div class="app">
    <h1>Bar Chart</h1>
    <bar-chart :chart-data="datacollection"></bar-chart>
    <button class="button is-primary" @click="fillData()">Randomize</button>
  </div>
</template>
<script>
import BarChart from './BarChart'
import { Tween, Easing } from 'tween.js'

// Exporting this so it can be used in other components
export default {
  name: 'Graph',
  components: {
    BarChart
  },
  data () {
    return {
      // instantiating datacollection with null
      datacollection: null
    }
  },
  created () {
    // anytime the vue instance is created, call the fillData() function.
    this.fillData()
    console.log('created')
  },
  methods: {
    fillData () {
      this.datacollection = {
        // Data for the y-axis of the chart
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            // Data for the x-axis of the chart
            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
          }
        ],
        count: 0
      }
    },
    getRandomInt () {
      // JS function to generate numbers to be used for the chart
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  },
  mounted () {
    const vm = this
    new Tween({ tweeningNumber: 0 })
      .easing(Easing.Quadratic.Out)
      .to({ tweeningNumber: 1000 }, 5000)
      .onUpdate(function () {
        console.log('hi')
        vm.datacollection.datasets.data[0] = this.tweeningNumber.toFixed(0)
      })
      .start()
    console.log(vm)
    vm.datacollection.datasets[0].data = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    vm.datacollection.count = vm.datacollection.count + 1
    vm.datacollection = {
      // Data for the y-axis of the chart
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#f87979',
          // Data for the x-axis of the chart
          data: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        }
      ],
      count: 0
    }
    // console.log(vm)
    // setTimeout(10, function () {
    //   console.log('changed')
    //   vm.datacollection.datasets.data[0] = 100
    // })
  }
}
</script>

<style scoped>

</style>
