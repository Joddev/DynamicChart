<template>
  <div class="back">
    <!--<img class="background" src="../assets/colorful-world.png">-->
    <div class="background"></div>
    <div class="title">
      <h1>Top 10 Countries By Electricity Consumption per capita</h1>
    </div>
    <div class="detail-value">unit: kWh</div>
    <chart v-bind="chart"></chart>
  </div>
</template>

<script>
import { stats, maximum, dates } from '../data/electricityPerCapita'
import labelInfo from '../data/flagInfo'
import chart from './DynamicChart.vue'

export default {
  data: function () {
    return {
      chart: {
        stats: stats,
        labelInfo: labelInfo,
        date: dates,
        interval: 5 * 1000,
        scale: 1000,
        maximum: maximum,
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
  body {
    text-shadow: 0 0 10px #000;
    color: #fff;
  }
  .back {
    width: 2400px;
  }
  .background {
    position: absolute;
    left: 0%;
    width: 85%;
    height: 100%;
    z-index: -3;
    background-color: #000;
    padding: 10%;
  }
  .title {
    font-size: 40px;
    padding-top: 1px;
  }
  .representative {
    background-size: 400px;
    width: 400px;
    height: 400px;
    position: absolute;
    top: 550px;
    right: 170px;
    font-size: 120px;
    z-index: 20;
  }
  .detail-value {
    font-size: 30px;
    font-weight: 600;
    position: absolute;
    left: 1950px;
    top: 230px;
    width: 300px;
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
