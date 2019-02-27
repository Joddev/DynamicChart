<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
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
