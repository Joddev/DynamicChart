<template>
  <div id="container" class="item-container" style="height: 500px">
    <div id="year" class="year"></div>
    <div class="representative"></div>
    <div class="additional">
      <table>
        <thead>{{additionalTitle}}</thead>
        <tbody id="additional-info"></tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Shuffle from 'shufflejs'
import TWEEN from 'tween.js'

// Setup the animation loop.
function animate (time) {
  requestAnimationFrame(animate)
  TWEEN.update(time)
}
requestAnimationFrame(animate)

export default {
  name: 'DynamicChart',
  props: {
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
      elementMap: {},
      elementList: [],
      instance: null,
      blurMap: {},
      scaleList: [],
      scaleUnit: 1,
      nullNumber: -12345,
      iconOnBarSize: 70
    }
  },
  created: function () {
    this.scaleUnit = this.scale
  },
  methods: {
    setAdditionalInfo: function (list, amount) {
      // TODO complete additional info
      const tbody = document.getElementById('additional-info')
      const count = tbody.childElementCount
      const need = amount - count
      for (let i = 0; i < need; i++) tbody.innerHTML += '<tr><td></td></tr>'
      const rows = tbody.children
      for (let i = 0; i < amount; i++) {
        const label = list[i].children[0].textContent
        rows[i].innerHTML = `<span class="additional-label">${label}:</span> ${this.elementMap[label].additional} ${this.additionalUnit}`
      }
    },
    /**
     * get label from node
     * @param {HTMLElement} node
     * @return {string} - node label
     */
    $_getNodeLabel: function (node) {
      return node.children[0].textContent
    },
    /**
     * get value from node
     * @param {HTMLElement} node
     * @return {number} - node value
     */
    $_getNodeValue: function (node) {
      return this.elementMap[this.$_getNodeLabel(node)].value
    },
    /**
     * get bar HTMLElement from node
     * @param {HTMLElement} node
     * @return {HTMLElement} - bar element
     */
    $_getNodeBar: function (node) {
      return node.children[1]
    },
    /**
     * get label on bar HTMLElement from node
     * @param {HTMLElement} node
     * @return {HTMLElement}
     */
    $_getNodeLabelOnBar: function (node) {
      return node.children[2].children[0].children[0]
    },
    /**
     * get icon on bar HTMLElement from node
     * @param {HTMLElement} node
     * @return {HTMLElement}
     */
    $_getNodeIconOnBar: function (node) {
      return node.children[2].children[0].children[1]
    },
    /**
     * get bar width
     * front width is affected by current max value
     * back width is affected by total max value
     * @param {number} cur - target value
     * @param {number} max - max value
     * @param {number} [min] - min value
     */
    $_getWidth: function (cur, max, min = 0) {
      const maximum = Math.max(max, this.maximum)
      const frontWidth = 0.65
      const backWidth = 0.15
      if (this.dynamic) return (((cur - min) / (max - min)) * frontWidth + (cur / maximum) * backWidth)
      else return ((cur / max) * frontWidth + (cur / maximum) * backWidth)
    },
    /**
     * set bar width by current value
     */
    $_setWidth: function () {
      const elementListSorted = this.elementList.slice().sort((n1, n2) => {
        return this.$_getNodeValue(n2) - this.$_getNodeValue(n1)
      })
      const topElement = elementListSorted[0]
      const max = this.$_getNodeValue(topElement)
      const min = this.dynamic ? this.$_getNodeValue(elementListSorted[this.limit - 1]) * 0.9 : 0
      const margin = this.limit === 15 ? 55 : 70
      // set representative image
      document.getElementsByClassName('representative')[0].style.backgroundImage = `url('${this.labelInfo[this.$_getNodeLabel(topElement)].img}')`
      // to handle equal value problems
      if (this.$_getNodeValue(topElement) === this.$_getNodeValue(elementListSorted[1])) this.elementMap[this.$_getNodeLabel(topElement)].value += 0.001
      // set width each
      for (let i = 0; i < elementListSorted.length; i++) {
        const element = elementListSorted[i]
        if (i < this.limit) {
          const width = this.$_getWidth(this.$_getNodeValue(element), max, min)
          this.$_getNodeBar(element).style.width = width * 100 + 'vw'
          // label on bar exceeds bar size
          if (this.$_getNodeBar(element).offsetWidth - margin < element.children[2].children[0].offsetWidth) {
            this.$_getNodeLabelOnBar(element).style.opacity = 0
          } else if (this.$_getNodeLabelOnBar(element).style.opacity === '0') {
            this.$_getNodeLabelOnBar(element).style.opacity = 1
          }
          // icon on bar excceds bar size
          if (this.$_getNodeBar(element).offsetWidth < 70) this.$_getNodeIconOnBar(element).style.opacity = 0
          else this.$_getNodeIconOnBar(element).style.opacity = 1
          // set bar visible
          if (element.style.display !== 'table') element.style.display = 'table'
        } else {
          const label = this.$_getNodeLabel(element)
          if (element.style.display !== 'none') {
            element.style.opacity = 0
            // set bar invisible
            if (!this.blurMap[label]) {
              this.blurMap[label] = setTimeout(() => {
                element.style.display = 'none'
                this.blurMap[label] = null
              }, this.tweening ? 1000 : 0)
            }
          }
        }
      }
      if (this.additional) this.setAdditionalInfo(elementListSorted, this.additionalLimit)
      // set scale
      const leftMargin = 11
      const start = this.scaleList.length ? this.scaleList[this.scaleList.length - 1].value + this.scaleUnit : this.scaleUnit
      for (let value = start; value < max * 1.1; value += this.scaleUnit) {
        const element = this.$_createScale(value)
        this.scaleList.push({
          value: value,
          node: element
        })
        document.getElementById('container').appendChild(element)
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
    /**
     * create scale element
     * @param {number} num - scale value
     * @return {HTMLElement} scale element
     */
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
    /**
     * get node value label
     * @param {HTMLElement} node
     * @return {HTMLElement} node value label
     */
    $_getNodeValueLabel: function (node) {
      return node.children[3]
    },
    /**
     * set node value label
     * @param {HTMLElement} node
     * @param {number} value
     */
    $_setNodeValueLabel: function (node, value) {
      this.$_getNodeValueLabel(node).innerHTML = this.$_numberWithCommas(value.toFixed(this.fixed)) + this.unit
    },
    /**
     * create node element
     * @param {{label: string, value: (number|string)}} data
     * @return {HTMLElement} created node element
     */
    $_createNode: function (data) {
      var div = document.createElement('div')
      let color, img
      try {
        color = this.labelInfo[data.label].color
        img = this.labelInfo[data.label].img
      } catch (err) {
        console.log(data.label)
        color = this.$_getRandomColor()
        img = 'https://banner2.kisspng.com/20171216/0a6/question-mark-png-5a352b58b02c08.4921308315134339447216.jpg'
      }
      div.innerHTML = `
          <div id="item-id-${data.label}" class="item limit-${this.limit}" style="width: 100%; display: none">
            <div class="item-label limit-${this.limit}">${data.label}</div>
            <div class="item-bar limit-${this.limit}" style="background: ${color}"></div>
            <div class="item-icon limit-${this.limit}"><div class="item-marker"><span>${data.label}</span><img src="${img}"></div></div>
            <div class="item-value limit-${this.limit}">${this.$_numberWithCommas(data.value.toFixed(this.fixed))}</div>
          </div>
      `.trim()

      this.elementList.push(div.firstChild)
      // Change this to div.childNodes to support multiple top-level nodes
      return div.firstChild
    },
    /**
     * create node element
     * @param {{label: string, value: (number|string)}} data
     * @return {object} created node element object
     */
    $_createElement: function (data) {
      if (data.value !== '-') {
        data.value = Number(data.value)
        this.elementMap[data.label] = {
          value: data.value,
          node: this.$_createNode(data),
          additional: data.additional
        }
        const node = this.elementMap[data.label].node
        // register to shuffle object
        this.instance.element.appendChild(node)
        this.instance.add([node])
      }
    },
    /**
     * @return {string} color
     */
    $_getRandomColor: function () {
      const letters = '0123456789ABCDEF'
      let color = '#'
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
      }
      return color
    },
    /**
     * number comma by thousands
     * @param {number} x
     */
    $_numberWithCommas: function (x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
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
      this.$_createElement(curData)
    }
    this.instance.sort({
      by: (element) => {
        return this.$_getNodeValue(element)
      },
      reverse: true
    })

    // to block initial label overflow
    this.$_setWidth()
    this.$_setWidth()

    let index = 1
    setTimeout(() => {
      const loop = setInterval(() => {
        if (index < this.stats.length) {
          document.getElementById('year').textContent = this.date[index]
          if (this.tweening) {
            const fromTweening = {}
            const toTweening = {}
            for (const i in this.stats[index]) {
              const curData = this.stats[index][i]
              let prevData = this.elementMap[curData.label]
              if (typeof (prevData) === 'undefined') {
                const initial = {
                  label: curData.label,
                  value: 0
                }
                this.$_createElement(initial)
                prevData = this.elementMap[curData.label]
              }
              if (curData.value !== '-') {
                let textColor = '#FFF'
                if (prevData.value > curData.value) textColor = '#F00'
                // if there is no prev data, set value label immediately
                if (prevData.value === this.nullNumber) {
                  prevData.value = curData.value
                  this.$_setNodeValueLabel(prevData.node, Number(curData.value))
                }
                fromTweening[curData.label] = prevData.value
                toTweening[curData.label] = Number(curData.value)
                this.$_getNodeValueLabel(prevData.node).style.color = textColor
              } else {
                prevData.value = this.nullNumber
              }
            }
            // set null unranked elements
            for (const label in this.elementMap) {
              if (!fromTweening[label]) this.elementMap[label].value = this.nullNumber
            }
            new TWEEN.Tween(fromTweening)
              .to(toTweening, this.interval * 0.99)
              .easing(TWEEN.Easing.Linear.None)
              .onUpdate(() => {
                for (const label in fromTweening) {
                  const value = fromTweening[label]
                  this.elementMap[label].value = value
                  this.$_setNodeValueLabel(this.elementMap[label].node, value)
                }
                this.$_setWidth()
              })
              .start()
          } else {
            // TODO
            // initialize
            for (const name in this.elementMap) {
              this.elementMap[name].value = 0
              this.elementMap[name].addtional = 0
              this.$_setNodeValueLabel(this.elementMap[name].node, 0)
            }
            for (const i in this.stats[index]) {
              const curData = this.stats[index][i]
              let prevData = this.elementMap[curData.label]
              if (typeof (prevData) === 'undefined') {
                const initial = {
                  label: curData.label,
                  value: 0,
                  additional: 0
                }
                this.$_createElement(initial)
                prevData = this.elementMap[curData.label]
              }
              prevData.value = Number(curData.value)
              prevData.additional = Number(curData.additional)
              this.$_setNodeValueLabel(prevData.node, Number(curData.value))
            }
            this.$_setWidth()
          }
          // additional
          if (this.additionalStats.length > 0) {
            //
          }
        } else {
          clearInterval(loop)
        }
        index++
      }, this.interval)
    }, 3000)

    setInterval(() => {
      this.instance.sort({
        by: (element) => {
          return this.$_getNodeValue(element)
        },
        reverse: true
      })
    }, 100)
  }
}
</script>

<style>
  .item-container {
    font-family: sans-serif;
    font-size: 1.25vw;
  }
  .item-label {
    display: table-cell;
    width: 10vw;
    height: 3vw;
    line-height: 3vw;
    text-align: right;
    padding-right: 1vw;
  }
  .item-bar {
    display: table-cell;
    height: 3vw;
  }
  .item-value {
    display: table-cell;
    text-align: left;
    padding-left: 0.5vw;
  }
  .item-icon {
    width: 10vw;
    height: 100%;
    position: absolute;
  }
  .item-icon .item-marker {
    position: absolute;
    width: 100%;
    right: 135%;
    top: 20%;
    text-align: right;
  }
  .item-icon img {
    position: absolute;
    width: 3vw;
    top: -0.6vw;
  }
  .item-icon span {
    margin-right: 0.5vw;
    white-space:nowrap;
    display: inline-block;
  }
  .item {
    /* font-size: 4vw; */
    font-weight: 600;
    display: inline;
    margin: 0.4vw;
  }
  .year {
    position: absolute;
    top: 33vw;
    left: 85vw;
    font-size: 4vw;
    z-index: 20;
    font-weight: 600;
  }
  .scale {
    position: absolute;
    z-index: -1;
    font-size: 0.75vw;
  }
  .scale-bar {
    position: absolute;
    width: 0.2vw;
    height: 38vw;
    background: rgba(171, 171, 171, 0.8);
  }
  .scale-value {
    position: absolute;
    width: 5vw;
    top: 38.5vw;
    left: -2.6vw;
    text-align: center;
    font-weight: 800;
  }
</style>
