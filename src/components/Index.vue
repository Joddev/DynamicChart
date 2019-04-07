<template>
  <div class="back">
    <!--<img class="background" src="../assets/colorful-world.png">-->
    <div class="background"></div>
    <div class="title">
      <h1>Top 10 Industrial Countries (% of total employment)</h1>
    </div>
    <!--<div class="detail-value">unit: kWh</div>-->
    <chart v-bind="chart"></chart>
  </div>
</template>

<script>
import { stats, maximum, dates } from '../data/result'
import labelInfo from '../data/flagInfo'
import chart from './DynamicChart.vue'

export default {
  data: function () {
    return {
      chart: {
        stats: stats,
        labelInfo: labelInfo,
        date: dates,
        interval: 0.5 * 1000,
        scale: 10,
        maximum: maximum,
        limit: 10,
        fixed: 2,
        unit: '%',
        dynamic: true
        // additionalStats: additionalStats,
        // additionalCand: ['World', 'Europe area', 'East Asia & Pacific', 'North America', 'OECD members', 'European Union', 'Middle East & North Africa'],
        // additionalLimit: 3,
        // additionalUnit: '%'
      }
    }
  },
  components: {
    chart
  }
}
</script>

<style>
  body {
    text-shadow: 0 0 10px #000;
    color: #fff;
  }
  .back {
    width: 100vw;
  }
  .background {
    position: absolute;
    left: 0%;
    width: 100%;
    height: 100%;
    z-index: -3;
    background-color: #000;
  }
  .title {
    font-size: 1.75vw;
    padding-top: 1px;
    text-align: center;
  }
  .representative {
    background-size: 15vw;
    width: 15vw;
    height: 15vw;
    position: absolute;
    top: 21vw;
    left: 81vw;
    z-index: 20;
  }
  .detail-value {
    font-size: 1vw;
    font-weight: 600;
    position: absolute;
    left: 83vw;
    top: 8vw;
    width: 15vw;
    text-align: right;
  }
  .additional {
    position: absolute;
    top: 370px;
    left: 1915px;
    text-align: right;
    width: 300px;
    font-size: 30px;
    font-weight: 700;
  }
  .additional thead {
    font-size: 40px;
    text-shadow: -1px 0 blue, 0 1px blue, 1px 0 blue, 0 -1px blue;
  }
  .additional table {
    width: 100%;
  }
</style>
