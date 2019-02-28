<template>
  <div id="container" class="item-container" style="height: 500px">
    <div id="year" class="year">2017</div>
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
  name: 'varative-chart',
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
    }
  },
  data: function () {
    return {
      elementMap: {},
      elementList: [],
      instance: null,
      blurMap: {},
      scaleList: [],
      scaleUnit: 1
    }
  },
  created: function () {
    this.scaleUnit = this.scale
  },
  methods: {
    getNodeValue: function (node) {
      const label = node.children[0].textContent
      return this.elementMap[label].value
    },
    getWidth: function (cur, max) {
      const maximum = Math.max(max, this.maximum)
      const maxWidth = 1600
      const tailWidth = 200
      return ((cur / max) * maxWidth + (cur / maximum) * tailWidth).toFixed(2)
    },
    setWidth: function () {
      const newList = this.elementList.concat().sort((n1, n2) => {
        return this.getNodeValue(n2) - this.getNodeValue(n1)
      })
      const max = this.getNodeValue(newList[0])
      for (let i = 0; i < newList.length; i++) {
        const element = newList[i]
        if (i < this.limit) {
          const width = this.getWidth(this.getNodeValue(element), max)
          element.children[1].style.width = width + 'px'
          if (width - 55 < element.children[2].children[0].offsetWidth) {
            element.children[2].children[0].children[0].style.opacity = 0
          }
          if (element.children[2].children[0].children[0].style.opacity === '0' && width - 55 >= element.children[2].children[0].offsetWidth) {
            element.children[2].children[0].children[0].style.opacity = 1
          }
          if (element.style.display !== 'table') {
            element.style.display = 'table'
          }
        } else {
          const label = element.children[0].textContent
          if (element.style.display !== 'none') {
            element.style.opacity = 0
            if (!this.blurMap[label]) {
              this.blurMap[label] = setTimeout(() => {
                element.style.display = 'none'
                this.blurMap[label] = null
              }, 1000)
            }
          }
        }
      }
      const leftMargin = 215
      let start = this.scaleUnit
      if (this.scaleList.length) {
        start = this.scaleList[this.scaleList.length - 1].value + this.scaleUnit
      }
      for (let value = start; value < max * 1.1; value += this.scaleUnit) {
        const element = this.createScale(value)
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
      for (let i = 0; i < this.scaleList.length; i++) {
        const scale = this.scaleList[i]
        if (scale.value > max * 1.1) scale.node.style.display = 'none'
        else {
          scale.node.style.display = ''
          scale.node.style.left = Number(this.getWidth(scale.value, max)) + leftMargin + 'px'
        }
      }
    },
    createScale: function (num) {
      const div = document.createElement('div')
      div.innerHTML = `
        <div id="scale-${num}" class="scale">
          <div class="scale-bar"></div>
          <div class="scale-value">${this.numberWithCommas(num)}</div>
        </div>
      `
      return div.firstElementChild
    },
    setNodeValue: function (node, value) {
      node.children[3].innerHTML = value
    },
    createNode: function (data) {
      var div = document.createElement('div')
      let color, img
      try {
        color = this.labelInfo[data.label].color
        img = this.labelInfo[data.label].img
      } catch (err) {
        console.log(data.label)
        color = this.getRandomColor()
        img = 'https://banner2.kisspng.com/20171216/0a6/question-mark-png-5a352b58b02c08.4921308315134339447216.jpg'
      }
      div.innerHTML = `
          <div id="item-id-${data.label}" class="item" style="width: 100%; display: none">
            <div class="item-label">${data.label}</div>
            <div class="item-bar" style="background: ${color}"></div>
            <div class="item-icon"><div class="item-marker"><span>${data.label}</span><img src="${img}"></div></div>
            <div class="item-value">${this.numberWithCommas(data.value.toFixed(this.fixed))}</div>
          </div>
      `.trim()

      this.elementList.push(div.firstChild)
      // Change this to div.childNodes to support multiple top-level nodes
      return div.firstChild
    },
    createElement: function (data) {
      if (data.value !== '-') {
        data.value = Number(Number(data.value).toFixed(this.fixed))
        this.elementMap[data.label] = {
          value: data.value,
          node: this.createNode(data)
        }
        const node = this.elementMap[data.label].node
        this.instance.element.appendChild(node)
        this.instance.add([node])
      }
    },
    getRandomColor: function () {
      var letters = '0123456789ABCDEF'
      var color = '#'
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
      }
      return color
    },
    numberWithCommas: function (x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
    }
  },
  mounted () {
    this.instance = new Shuffle(document.getElementById('container'), {
      itemSelector: '.item',
      speed: this.shuffleSpeed
    })

    document.getElementById('year').textContent = this.date[0]
    for (const i in this.stats[0]) {
      const curData = this.stats[0][i]
      this.createElement(curData)
    }

    this.setWidth()
    this.instance.sort({
      by: (element) => {
        return this.getNodeValue(element)
      },
      reverse: true
    })

    let index = 1
    const loop = setInterval(() => {
      if (index < this.stats.length) {
        document.getElementById('year').textContent = this.date[index]
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
            this.createElement(initial)
            prevData = this.elementMap[curData.label]
          }
          if (curData.value !== '-') {
            fromTweening[curData.label] = prevData.value
            toTweening[curData.label] = curData.value
          }
          let textColor = '#000'
          if (prevData.value > curData.value) textColor = '#ff0000'
          prevData.node.children[3].style.color = textColor
        }
        new TWEEN.Tween(fromTweening)
          .to(toTweening, this.interval * 0.99)
          .easing(TWEEN.Easing.Linear.None)
          .onUpdate(() => {
            for (const label in fromTweening) {
              const value = Number(fromTweening[label].toFixed(this.fixed))
              this.elementMap[label].value = value
              this.setNodeValue(this.elementMap[label].node, this.numberWithCommas(value))
            }
            this.setWidth()
          })
          .start()
      } else {
        clearInterval(loop)
      }
      index++
    }, this.interval)

    setInterval(() => {
      this.instance.sort({
        by: (element) => {
          return this.getNodeValue(element)
        },
        reverse: true
      })
    }, 200)
  }
}
</script>

<style>
  .item-container {
    font-family: sans-serif
  }
  .item-label {
    display: table-cell;
    width: 200px;
    height: 30px;
    line-height: 30px;
    text-align: right;
    padding-right: 10px;
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
    width: 60px;
    position: absolute;
  }
  .item-icon .item-marker {
    position: absolute;
    right: 113px;
    top: 6px;
  }
  .item-icon span {
    margin-right: 5px;
    line-height: 40px;
    white-space:nowrap;
    display: inline-block;
  }
  .item-icon img {
    width: 50px;
    position: absolute;
  }
  .item {
    font-size: 30px;
    font-weight: 600;
    display: inline;
    margin: 5px;
  }
  .year {
    position: absolute;
    top: 800px;
    right: 300px;
    font-size: 100px;
    z-index: 20;
    font-weight: 600;
  }
  .scale {
    position: absolute;
    left: 208.5px;
    z-index: -1
  }
  .scale-bar {
    position: absolute;
    width: 3px;
    height: 1020px;
    background: rgba(171, 171, 171, 0.8);
  }
  .scale-value {
    position: absolute;
    width: 200px;
    left: -100px;
    top: 1025px;
    text-align: center;
    font-size: 20px;
    font-weight: 800;
    color: rgba(116, 116, 116, 0.8);
  }
</style>
