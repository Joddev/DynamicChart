<template>
  <div class="back">
    <!--<img class="background" src="../assets/colorful-world.png">-->
    <div class="background"></div>
    <div class="title">
      <h1>Top 10 Net National Income per capita ($)</h1>
    </div>
    <chart v-bind="chart"></chart>
  </div>
</template>

<script>
import stats from '../data/adjustedNetNationalIncomePerCapita'
import labelInfo from '../data/flagInfo'
import chart from './VarativeChart.vue'

export default {
  data: function () {
    return {
      chart: {
        stats: stats,
        labelInfo: labelInfo,
        date: (() => {
          const date = []
          for (let i = 1970; i <= 2016; i++) date.push(i)
          return date
        })(),
        interval: 8 * 1000,
        scale: 5000,
        maximum: 82020,
        limit: 10,
        fixed: 2
      }
    }
  },
  components: {
    chart
  }
}
</script>

<style>
.back {
  width: 2400px;
}
.background {
  position: absolute;
  left: 0%;
  width: 85%;
  height: 100%;
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
