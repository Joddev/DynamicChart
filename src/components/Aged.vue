<template>
  <div class="back">
    <!--<img class="background" src="../assets/colorful-world.png">-->
    <div class="background"></div>
    <div class="title">
      <h1>Top 10 Most Aged Country</h1>
    </div>
    <div class="theme"></div>
    <div class="explanation">ratio = (aged over 64) / (aged 15 - 64)</div>
    <chart v-bind="chart"></chart>
  </div>
</template>

<script>
import { stats, maximum, dates } from '../data/aged'
import labelInfo from '../data/flagInfo'
import chart from './DynamicChart.vue'

export default {
  data: function () {
    return {
      chart: {
        stats: stats,
        labelInfo: labelInfo,
        date: dates,
        interval: 3 * 1000,
        scale: 10,
        maximum: maximum,
        limit: 10,
        fixed: 2,
        dynamic: true,
        unit: '%'
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
.theme {
  position: absolute;
  opacity: 0.4;
  bottom: 150px;
  left: 1400px;
}
.explanation {
  position: absolute;
  bottom: 173px;
  left: 1235px;
  font-size: 30px;
  width: 1000px;
  text-align: right;
  color: #777;
  font-weight: bold;
}
.theme img{
  width:800px;
}
</style>
