<template>
  <div id="wrapper">
    <div id="container" class="item-container" style="height: 500px; overflow:visible;">
      <template v-if="barType == 'barWithImageLeft'">
        <template v-for="bar in barList">
          <barWithImageLeft :ref="'bars'" :key="bar.label" v-bind="bar"></barWithImageLeft>
        </template>
      </template>
      <div id="year" class="year"></div>
      <div class="representative"></div>
      <div class="additional">
        <table>
          <thead>{{additionalTitle}}</thead>
          <tbody id="additional-info"></tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Shuffle from 'shufflejs'
import TWEEN from 'tween.js'
import barWithImageLeft from './BarWithImageLeft'

// Setup the animation loop.
function animate (time) {
  requestAnimationFrame(animate)
  TWEEN.update(time)
}
requestAnimationFrame(animate)

export default {
  name: 'DynamicChart',
  props: {
    barType: {
      type: String,
      default: 'barWithImageLeft',
      validator: function (value) {
        return ['barWithImageLeft'].indexOf(value) !== -1
      }
    },
    interval: {
      type: Number,
      default: 2 * 1000
    },
    limit: {
      type: Number,
      default: 15
    },
    shuffleSpeed: {
      type: Number,
      default: 1000
    },
    stats: {
      type: Array
    },
    labelInfo: {
      type: Object
    },
    date: {
      type: Array
    },
    fixed: {
      type: Number,
      default: 0
    },
    scale: {
      type: Number,
      default: 500000000
    },
    maximum: {
      type: Number,
      default: 0
    },
    dynamic: {
      type: Boolean,
      default: false
    },
    unit: {
      type: String,
      default: ''
    },
    tweening: {
      type: Boolean,
      default: true
    },
    additional: {
      type: Boolean,
      default: false
    },
    additionalLimit: {
      type: Number,
      default: 0
    },
    additionalTitle: {
      type: String,
      default: ''
    },
    additionalStats: {
      type: Array,
      default: () => []
    },
    additionalUnit: {
      type: String,
      default: ''
    },
    additionalCand: {
      type: Array,
      default: () => []
    }
  },
  data: function () {
    return {
      barList: [],
      instance: null,
      scaleList: [],
      scaleUnit: 1,
      nullNumber: -123456
    }
  },
  created: function () {
    this.scaleUnit = this.scale
    this.$options.barDict = {}
  },
  updated: function () {
    this.$refs['bars'].forEach((vue) => {
      if (!(vue.label in this.$options.barDict)) {
        this.$options.barDict[vue.label] = vue
        this.instance.add([vue.$el])
      }
    })
  },
  methods: {
    $_getBarValue: function (element) {
      const label = element.id.slice(8)
      if (this.$options.barDict[label]) {
        return this.$options.barDict[label].value
      } else {
        console.log(label)
        console.log(this.$options.barDict)
        return 0
      }
    },
    $_getWidth: function (cur, max, min = 0) {
      const maximum = Math.max(max, this.maximum)
      const frontWidth = 0.60
      const backWidth = 0.15
      if (this.dynamic) return (((cur - min) / (max - min)) * frontWidth + (cur / maximum) * backWidth) * 100
      else return ((cur / max) * frontWidth + (cur / maximum) * backWidth) * 100
    },
    $_setRepresentativeImg: function (element) {
      if (this.labelInfo[this.$_getNodeTeam(element)]) {
        document.getElementsByClassName('representative')[0].style.backgroundImage = `url('${this.labelInfo[this.$_getNodeLabel(element)].img}')`
      } else {
        document.getElementsByClassName('representative')[0].style.backgroundImage = `url('${this.labelInfo[this.$_getNodeTeam(element)].img}')`
      }
    },
    $_setScale: function (max, min) {
      const leftMargin = 11
      const start = this.scaleList.length ? this.scaleList[this.scaleList.length - 1].value + this.scaleUnit : this.scaleUnit
      for (let value = start; value < max * 1.1; value += this.scaleUnit) {
        const element = this.$_createScale(value)
        this.scaleList.push({
          value: value,
          node: element
        })
        document.getElementById('wrapper').appendChild(element)
      }
      if (this.scaleList.length > 8) {
        this.scaleUnit = this.scaleUnit * 2
        this.scaleList.forEach(scale => {
          if (scale.value % this.scaleUnit !== 0) scale.node.remove()
        })
        this.scaleList = this.scaleList.filter(scale => scale.value % this.scaleUnit === 0)
      }
      for (const scale of this.scaleList) {
        if (scale.value > max * 1.1 || scale.value < min) scale.node.style.display = 'none'
        else {
          scale.node.style.display = ''
          scale.node.style.left = Number(this.$_getWidth(scale.value, max, min) * 100) + leftMargin + 'vw'
        }
      }
    },
    $_adjustWidth: function () {
      const bars = Object.values(this.$options.barDict).sort((v1, v2) => v2.value - v1.value)
      if (bars.length > 0) {
        const top = bars[0]
        const max = top.value
        const min = this.dynamic ? bars[this.limit - 1] * 0.9 : 0

        // to handle the equal value problem
        // top.value = top.value + 0.00000000000001
        for (const [i, v] of bars.entries()) {
          if (i < this.limit) {
            const width = this.$_getWidth(v.value, max, min)
            v.visible()
            v.setWidth(width + 'vw')
          } else {
            v.invisible()
          }
        }
      }
    },
    $_createScale: function (num) {
      const div = document.createElement('div')
      div.innerHTML = `
        <div id="scale-${num}" class="scale">
          <div class="scale-bar"></div>
          <div class="scale-value">${this.$_numberWithCommas(num) + this.unit}</div>
        </div>
      `
      return div.firstElementChild
    },
    $_createBar: function (data) {
      const value = parseFloat(data.value)
      if (!isNaN(value)) {
        const { color, img } = this.$_getBarLabelInfo(data)
        const bar = {
          label: data.label,
          value: value,
          color: color,
          img: img,
          size: 10,
          fixed: this.fixed
        }
        this.barList.push(bar)
      }
    },
    $_getBarLabelInfo: function (data) {
      if (data.team) {
        const info = this.labelInfo[data.team]
        if (info) return info
      }
      if (data.label) {
        const info = this.labelInfo[data.label]
        if (info) return info
      }
      throw new Error(`Unknown label ${data.label}`)
    },
    $_sortNodeBar: function () {
      this.instance.sort({
        by: (element) => {
          return this.$_getBarValue(element)
          // return this.$_getNodeValue(element)
        },
        reverse: true
      })
    },
    $_getBarObject: function (label) {
      return this.barList.find(bar => bar.label === label)
    }
  },
  mounted () {
    this.instance = new Shuffle(document.getElementById('container'), {
      itemSelector: '.item',
      speed: this.shuffleSpeed
    })
    // set initial data
    document.getElementById('year').textContent = this.date[0]
    for (const i in this.stats[0]) {
      const curData = this.stats[0][i]
      curData.value = Number(curData.value)
      this.$_createBar(curData)
    }

    this.$_sortNodeBar()

    let index = 1
    setTimeout(() => {
      const loop = setInterval(() => {
        if (index < this.stats.length) {
          document.getElementById('year').textContent = this.date[index]
          const before = {}
          const after = {}
          for (const stat of this.stats[index]) {
            let prevData = this.$options.barDict[stat.label]
            if (!prevData) {
              prevData = {
                label: stat.label,
                value: this.nullNumber,
                team: stat.team
              }
              this.$_createBar(prevData)
            }
            before[stat.label] = prevData.value
            after[stat.label] = parseFloat(stat.value) || 0
          }
          for (const label in this.$options.barDict) {
            if (before[label] === undefined) {
              before[label] = this.$options.barDict[label].value
              after[label] = 0
              this.$_getBarObject(label).value = 0
            }
          }
          new TWEEN.Tween(before)
            .to(after, this.interval * 0.99)
            .easing(TWEEN.Easing.Linear.None)
            .onUpdate(() => {
              for (const label in before) {
                const value = before[label]
                this.$_getBarObject(label).value = value
              }
              this.$_adjustWidth()
            })
            .start()
        } else {
          clearInterval(loop)
        }
        index++
      }, this.interval)
    }, 3000)

    setInterval(() => {
      this.$_sortNodeBar()
    }, 100)
  },
  components: {
    barWithImageLeft
  }
}
</script>

<style>
  .item-container {
    font-family: sans-serif;
    font-size: 1.25vw;
  }
  .year {
    position: absolute;
    top: 33vw;
    left: 80vw;
    font-size: 7vw;
    z-index: 20;
    font-weight: 600;
  }
  .scale {
    position: absolute;
    z-index: -1;
    font-size: 0.75vw;
    top: 10.5vw;
    color: #949494;
  }
  .scale-bar {
    position: absolute;
    /*top: -51vw;*/
    /*top: -800px;*/
    width: 0.2vw;
    /*height: 45vw;*/
    height: 42vw;
    background: rgba(171, 171, 171, 0.8);
  }
  .scale-value {
    position: absolute;
    width: 8vw;
    left: 0.5vw;
    text-align: left;
    font-weight: 800;
  }
</style>
