<template>
  <div id="container" style="width: 500px; height: 500px"></div>
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

const data = [[{'label': 'A', 'value': 7902}, {'label': 'B', 'value': 1400}, {'label': 'C', 'value': 8464}, {'label': 'D', 'value': 2191}, {'label': 'E', 'value': 5742}, {'label': 'F', 'value': 8386}, {'label': 'G', 'value': 7906}], [{'label': 'A', 'value': 8619}, {'label': 'B', 'value': 2651}, {'label': 'C', 'value': 4370}, {'label': 'D', 'value': 8109}, {'label': 'E', 'value': 7322}, {'label': 'F', 'value': 5270}, {'label': 'G', 'value': 4545}], [{'label': 'A', 'value': 2568}, {'label': 'B', 'value': 1700}, {'label': 'C', 'value': 9748}, {'label': 'D', 'value': 5992}, {'label': 'E', 'value': 2627}, {'label': 'F', 'value': 4432}, {'label': 'G', 'value': 7007}], [{'label': 'A', 'value': 9052}, {'label': 'B', 'value': 3647}, {'label': 'C', 'value': 4367}, {'label': 'D', 'value': 9793}, {'label': 'E', 'value': 8441}, {'label': 'F', 'value': 110}, {'label': 'G', 'value': 3844}], [{'label': 'A', 'value': 1286}, {'label': 'B', 'value': 7927}, {'label': 'C', 'value': 2223}, {'label': 'D', 'value': 7628}, {'label': 'E', 'value': 9401}, {'label': 'F', 'value': 9532}, {'label': 'G', 'value': 7985}], [{'label': 'A', 'value': 3874}, {'label': 'B', 'value': 773}, {'label': 'C', 'value': 5263}, {'label': 'D', 'value': 612}, {'label': 'E', 'value': 9793}, {'label': 'F', 'value': 5027}, {'label': 'G', 'value': 7745}], [{'label': 'A', 'value': 5092}, {'label': 'B', 'value': 7547}, {'label': 'C', 'value': 5008}, {'label': 'D', 'value': 9382}, {'label': 'E', 'value': 3726}, {'label': 'F', 'value': 4568}, {'label': 'G', 'value': 833}], [{'label': 'A', 'value': 8832}, {'label': 'B', 'value': 5088}, {'label': 'C', 'value': 6506}, {'label': 'D', 'value': 9266}, {'label': 'E', 'value': 7502}, {'label': 'F', 'value': 5067}, {'label': 'G', 'value': 7914}], [{'label': 'A', 'value': 3122}, {'label': 'B', 'value': 2428}, {'label': 'C', 'value': 524}, {'label': 'D', 'value': 3407}, {'label': 'E', 'value': 7844}, {'label': 'F', 'value': 2869}, {'label': 'G', 'value': 9855}], [{'label': 'A', 'value': 1381}, {'label': 'B', 'value': 3738}, {'label': 'C', 'value': 3486}, {'label': 'D', 'value': 9359}, {'label': 'E', 'value': 7355}, {'label': 'F', 'value': 5291}, {'label': 'G', 'value': 1933}], [{'label': 'A', 'value': 3301}, {'label': 'B', 'value': 6415}, {'label': 'C', 'value': 5782}, {'label': 'D', 'value': 3013}, {'label': 'E', 'value': 2919}, {'label': 'F', 'value': 6320}, {'label': 'G', 'value': 2290}], [{'label': 'A', 'value': 2787}, {'label': 'B', 'value': 6636}, {'label': 'C', 'value': 8877}, {'label': 'D', 'value': 7162}, {'label': 'E', 'value': 9008}, {'label': 'F', 'value': 6676}, {'label': 'G', 'value': 4436}], [{'label': 'A', 'value': 2814}, {'label': 'B', 'value': 3602}, {'label': 'C', 'value': 1139}, {'label': 'D', 'value': 2279}, {'label': 'E', 'value': 1194}, {'label': 'F', 'value': 9630}, {'label': 'G', 'value': 8964}], [{'label': 'A', 'value': 8211}, {'label': 'B', 'value': 9529}, {'label': 'C', 'value': 2484}, {'label': 'D', 'value': 7844}, {'label': 'E', 'value': 7529}, {'label': 'F', 'value': 5679}, {'label': 'G', 'value': 3525}], [{'label': 'A', 'value': 8698}, {'label': 'B', 'value': 1736}, {'label': 'C', 'value': 3162}, {'label': 'D', 'value': 9818}, {'label': 'E', 'value': 7472}, {'label': 'F', 'value': 9502}, {'label': 'G', 'value': 5177}], [{'label': 'A', 'value': 2779}, {'label': 'B', 'value': 6897}, {'label': 'C', 'value': 1608}, {'label': 'D', 'value': 1272}, {'label': 'E', 'value': 1042}, {'label': 'F', 'value': 7968}, {'label': 'G', 'value': 4854}], [{'label': 'A', 'value': 8126}, {'label': 'B', 'value': 3699}, {'label': 'C', 'value': 2109}, {'label': 'D', 'value': 6044}, {'label': 'E', 'value': 5117}, {'label': 'F', 'value': 3670}, {'label': 'G', 'value': 6950}], [{'label': 'A', 'value': 3538}, {'label': 'B', 'value': 8702}, {'label': 'C', 'value': 7390}, {'label': 'D', 'value': 8261}, {'label': 'E', 'value': 2497}, {'label': 'F', 'value': 7770}, {'label': 'G', 'value': 2910}], [{'label': 'A', 'value': 4153}, {'label': 'B', 'value': 2670}, {'label': 'C', 'value': 5514}, {'label': 'D', 'value': 6070}, {'label': 'E', 'value': 8280}, {'label': 'F', 'value': 8334}, {'label': 'G', 'value': 9338}], [{'label': 'A', 'value': 2028}, {'label': 'B', 'value': 6650}, {'label': 'C', 'value': 6672}, {'label': 'D', 'value': 6361}, {'label': 'E', 'value': 4163}, {'label': 'F', 'value': 9270}, {'label': 'G', 'value': 7209}]]
let instance = null

const elements = {}

const createElement = (data) => {
  elements[data.label] = {
    value: data.value,
    node: createNode(data)
  }
  const node = elements[data.label].node
  instance.element.appendChild(node)
  instance.add([node])
}

function getRandomColor () {
  var letters = '0123456789ABCDEF'
  var color = '#'
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)]
  }
  return color
}

const createNode = (data) => {
  var div = document.createElement('div')
  div.innerHTML = `
      <div id="item-id-${data.label}" class="item" style="width: 100%; display: table">
        <div class="item-icon">${data.label}</div>
        <div class="item-bar" style="background: ${getRandomColor()}"></div>
        <div class="item-value">${data.value}</div>
      </div>
  `.trim()

  // Change this to div.childNodes to support multiple top-level nodes
  return div.firstChild
}

const getNodeValue = (node) => {
  return Number(node.children[2].innerHTML)
}

const setNodeValue = (node, value) => {
  node.children[2].innerHTML = value
}

let prevMax = 0
const setWidth = (node) => {
  let max = 0
  const maxWidth = 400
  for (const label in elements) {
    if (max < elements[label].value) max = elements[label].value
  }
  if (Math.abs(max - prevMax) > 200) {
    console.log(prevMax)
    console.log(max)
  }
  prevMax = max
  for (const label in elements) {
    const width = ((elements[label].value / max) * maxWidth).toFixed(2)
    elements[label].node.children[1].style.width = width + 'px'
  }
}

export default {
  name: 'MyShuffle',
  mounted () {
    instance = new Shuffle(document.getElementById('container'), {
      itemSelector: '.item',
      columnWidth: 2
    })

    // Initial value
    for (const i in data[0]) {
      const curData = data[0][i]
      createElement(curData)
    }

    let index = 1
    const interval = setInterval(() => {
      console.log('START!!!!!')
      if (index < data.length) {
        for (const i in data[index]) {
          const curData = data[index][i]
          let prevData = elements[curData.label]
          if (typeof (prevData) === 'undefined') {
            const initial = {
              label: curData.label,
              value: 0
            }
            createElement(initial)
            prevData = elements[curData.label]
          }
          const tweening = {value: prevData.value}
          new TWEEN.Tween(tweening)
            .to({value: curData.value}, 2950)
            .easing(TWEEN.Easing.Quadratic.Out)
            .onUpdate(() => {
              // if (curData.label === 'A') {
              //   console.log(Number(tweening.value.toFixed(0)) - Number(prevData.value))
              // }
              prevData.value = Number(tweening.value.toFixed(0))
              setNodeValue(prevData.node, prevData.value)
              setWidth()
            })
            .start()
        }
      } else {
        clearInterval(interval)
      }
      index++
    }, 3000)

    setInterval(() => {
      instance.sort({
        by: (element) => {
          return getNodeValue(element)
        },
        reverse: true
      })
    }, 100)
  }
}
</script>

<style scoped>
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
