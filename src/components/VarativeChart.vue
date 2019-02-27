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
      default: []
    }
  },
  data: function () {
    return {
      elementMap: {},
      elementList: [],
      instance: null,
      blurMap: {}
    }
  },
  methods: {
    getNodeValue: function (node) {
      return Number(node.children[3].innerHTML) - 77
    },
    setWidth: function () {
      const newList = this.elementList.concat().sort((n1, n2) => {
        return this.getNodeValue(n2) - this.getNodeValue(n1)
      })
      const max = this.getNodeValue(newList[0])
      const maxWidth = 1500
      for (let i = 0; i < newList.length; i++) {
        const element = newList[i]
        if (i < this.limit) {
          const width = ((this.getNodeValue(element) / max) * maxWidth).toFixed(2)
          element.children[1].style.width = width + 'px'
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
            <div class="item-value">${data.value}</div>
          </div>
      `.trim()

      this.elementList.push(div.firstChild)
      // Change this to div.childNodes to support multiple top-level nodes
      return div.firstChild
    },
    createElement: function (data) {
      if (data.value !== '-') {
        data.value = Number(Number(data.value).toFixed(2))
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

    // Initial value
    const years = []
    for (let i = 1999; i <= 2016; i++) years.push(i)
    document.getElementById('year').textContent = years[0]
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
        document.getElementById('year').textContent = years[index]
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
        }
        new TWEEN.Tween(fromTweening)
          .to(toTweening, this.interval * 0.99)
          .easing(TWEEN.Easing.Linear.None)
          .onUpdate(() => {
            for (const label in fromTweening) {
              const value = Number(fromTweening[label].toFixed(2))
              this.elementMap[label].value = value
              this.setNodeValue(this.elementMap[label].node, value)
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
    right: 98px;
    top: 9px;
  }
  .item-icon span {
    margin-right: 5px;
    line-height: 22px;
    white-space:nowrap;
    display: inline-block;
  }
  .item-icon img {
    width: 40px;
    position: absolute;
  }
  .item {
    font-size: 25px;
    font-weight: 600;
    display: inline;
    margin: 10px;
  }
  .year {
    position: absolute;
    top: 800px;
    right: 300px;
    font-size: 100px;
    z-index: 20;
    font-weight: 600;
  }
</style>
