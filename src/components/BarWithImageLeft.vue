<template>
  <div v-bind:id="id" class="item" v-bind:class="[size.toString()]" style="">
    <div class="item-icon">
    <img v-bind:src="img">
    </div>
    <div class="item-bar" v-bind:style="{background: color}">
      <span class="item-label">{{ label }}</span>
    </div>
    <div class="item-value">{{ formattedValue }}</div>
  </div>
</template>

<script>
import { formatter } from './mixin/formatter'

export default {
  name: 'BarWithImageLeft',
  mixins: [formatter],
  props: {
    color: String,
    img: String,
    size: Number,
    label: String,
    value: Number,
    fixed: {
      type: Number,
      default: 0
    }
  },
  computed: {
    id: function () {
      return `item-id-${this.label}`
    },
    formattedValue: function () {
      return this.numberWithCommas(this.value.toFixed(this.fixed))
    },
    imgUrl: function () {
      return `url(${this.img})`
    }
  },
  methods: {
    setWidth: function (width) {
      this.$el.querySelector('.item-bar').style.width = width
    },
    invisible: function () {
      this.$el.style.opacity = 0
    },
    visible: function () {
      this.$el.style.opacity = 1
    }
  }
}
</script>

<style scoped>
  .item {
    /* font-size: 4vw; */
    font-weight: 600;
    /* display: inline; */
    /*margin: 0.25vw;*/
    /* margin: 0.5vw; */
    /* margin-left: 10.8vw; */
    position: relative;
    display: flex;
    flex-direction: row;
  }
  .item-label {
    width: 100%;
    height: 3vw;
    line-height: 3vw;
    /*height: 2.5vw;*/
    /*line-height: 2.5vw;*/
    color: #FFF;
    text-shadow: 0 0 10px #000;
    margin-right: 1vw;
  }
  .item-bar {
    height: 3vw;
    /*height: 2.5vw;*/
    text-align: right;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: clip;
    width: 10vw;
    /* display: flex; */
  }
  .item-value {
    /* display: flex; */
    text-align: left;
    padding-left: 0.5vw;
    line-height: 3vw;
    /*line-height: 2.5vw;*/
  }
  .item-icon {
    /* width: 3vw; */
    /* height: 3vw; */
    /* background-size: contain; */
    /* background-repeat: no-repeat; */
    /* height: 100%; */
    /* position: absolute; */
    padding-right: 1vw;
    /* display: flex; */
  }
  .item-icon .item-marker {
    /* position: absolute; */
    /*width: 100%;*/
    /*right: 135%;*/
    right: 105%;
    top: 20%;
    text-align: right;
  }
  .item-icon .item-marker span {
    color: #FFF;
    text-shadow: 0 0 10px #000;
  }
  .item-icon img {
    /* position: absolute; */
    width: auto;
    height: auto;
    max-height: 3vw;
    margin: 0;
    top: 0vw;
  }
  .item-icon span {
    margin-right: 0.5vw;
    white-space:nowrap;
    display: inline-block;
  }
</style>
