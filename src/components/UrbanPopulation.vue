<template>
  <div>
    <img class="background" src="../assets/colorful-world.png">
    <div class="title">
      <h1>Top 15 Country with Highest Urban Population</h1>
    </div>
    <chart v-bind="chart"></chart>
  </div>
</template>

<script>
import stats from '../data/urbanPopulation'
import labelInfo from '../data/flagInfo'
import chart from './DynamicChart.vue'

export default {
  name: 'life-expectancy',
  data: function () {
    return {
      chart: {
        stats: stats,
        labelInfo: labelInfo,
        date: (() => {
          const date = []
          for (let i = 1960; i <= 2017; i++) date.push(i)
          return date
        })(),
        interval: 4 * 1000,
        scale: 50000000
      }
    }
  },
  components: {
    chart
  }
}
</script>

<style>
.background {
  position: absolute;
  left: 0%;
  width: 85%;
  z-index: -3;
  opacity: 0.5;
  background-color: #e0dbcd8c;
  padding: 10%;
}
.title {
  font-size: 40px;
  padding-top: 1px;
}
</style>
