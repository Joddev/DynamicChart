<template>
  <div id="app">
    <img src="./assets/logo.png">
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
.item-icon {
  display: table-cell;
  width: 50px;
  height: 50px;
  line-height: 50px;
}
.item-bar {
  display: table-cell;
  width: 400px;
  height: 50px;
}
.item-value {
  display: table-cell;
}
</style>
