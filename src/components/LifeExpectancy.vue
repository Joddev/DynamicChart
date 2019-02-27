<template>
  <div>
    <img class="background" src="../assets/colorful-world.png">
    <div class="title">
      <h1>Top 15 Life Expectancy At Birth</h1>
    </div>
    <chart v-bind="chart"></chart>
  </div>
</template>

<script>
import stats from '../data/lifeExpectancy'
import labelInfo from '../data/flagInfo'
import chart from './VarativeChart.vue'

export default {
  name: 'life-expectancy',
  data: function () {
    return {
      chart: {
        stats: stats,
        labelInfo: labelInfo,
        date: [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
        interval: 8 * 1000
      }
    }
  },
  components: {
    chart
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.background {
  position: absolute;
  left: 5%;
  width: 85%;
  z-index: -3;
  opacity: 0.5;
}
.title {
  font-size: 40px
}
/* .item-label {
  display: table-cell;
  width: 50px;
  height: 30px;
  line-height: 30px;
}
.item-bar {
  display: table-cell;
  height: 30px;
}
.item-value {
  display: table-cell;
  text-align: left;
  padding: 10px;
}
.item-icon {
  margin: auto;
}
.item {
  display: inline;
  margin: 10px;
} */
</style>
