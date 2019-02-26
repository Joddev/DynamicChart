<template>
  <div id="container" class="item-container" style="height: 500px">
    <div id="year" class="year">2017</div>
  </div>
</template>

<script>
import Shuffle from 'shufflejs'
import TWEEN from 'tween.js'
import labelInfo from './FlagData.vue'
import data from './LifeExpectancy.vue'

// Setup the animation loop.
function animate (time) {
  requestAnimationFrame(animate)
  TWEEN.update(time)
}
requestAnimationFrame(animate)

// const data = [
//   [
//     {'label': 'A', 'value': 7902}, {'label': 'BBBB', 'value': 1400}, {'label': 'C', 'value': 8464}, {'label': 'D', 'value': 2191}, {'label': 'E', 'value': 5742}, {'label': 'F', 'value': 8386}, {'label': 'G', 'value': 7906}
//   ], [
//     {'label': 'A', 'value': 8619}, {'label': 'BBBB', 'value': 2651}, {'label': 'C', 'value': 4370}, {'label': 'D', 'value': 8109}, {'label': 'E', 'value': 7322}, {'label': 'F', 'value': 5270}, {'label': 'G', 'value': 4545}
//   ], [{'label': 'A', 'value': 2568}, {'label': 'BBBB', 'value': 1700}, {'label': 'C', 'value': 9748}, {'label': 'D', 'value': 5992}, {'label': 'E', 'value': 2627}, {'label': 'F', 'value': 4432}, {'label': 'G', 'value': 7007}], [{'label': 'A', 'value': 9052}, {'label': 'BBBB', 'value': 3647}, {'label': 'C', 'value': 4367}, {'label': 'D', 'value': 9793}, {'label': 'E', 'value': 8441}, {'label': 'F', 'value': 110}, {'label': 'G', 'value': 3844}], [{'label': 'A', 'value': 1286}, {'label': 'BBBB', 'value': 7927}, {'label': 'C', 'value': 2223}, {'label': 'D', 'value': 7628}, {'label': 'E', 'value': 9401}, {'label': 'F', 'value': 9532}, {'label': 'G', 'value': 7985}], [{'label': 'A', 'value': 3874}, {'label': 'BBBB', 'value': 773}, {'label': 'C', 'value': 5263}, {'label': 'D', 'value': 612}, {'label': 'E', 'value': 9793}, {'label': 'F', 'value': 5027}, {'label': 'G', 'value': 7745}], [{'label': 'A', 'value': 5092}, {'label': 'BBBB', 'value': 7547}, {'label': 'C', 'value': 5008}, {'label': 'D', 'value': 9382}, {'label': 'E', 'value': 3726}, {'label': 'F', 'value': 4568}, {'label': 'G', 'value': 833}], [{'label': 'A', 'value': 8832}, {'label': 'BBBB', 'value': 5088}, {'label': 'C', 'value': 6506}, {'label': 'D', 'value': 9266}, {'label': 'E', 'value': 7502}, {'label': 'F', 'value': 5067}, {'label': 'G', 'value': 7914}], [{'label': 'A', 'value': 3122}, {'label': 'BBBB', 'value': 2428}, {'label': 'C', 'value': 524}, {'label': 'D', 'value': 3407}, {'label': 'E', 'value': 7844}, {'label': 'F', 'value': 2869}, {'label': 'G', 'value': 9855}], [{'label': 'A', 'value': 1381}, {'label': 'BBBB', 'value': 3738}, {'label': 'C', 'value': 3486}, {'label': 'D', 'value': 9359}, {'label': 'E', 'value': 7355}, {'label': 'F', 'value': 5291}, {'label': 'G', 'value': 1933}], [{'label': 'A', 'value': 3301}, {'label': 'BBBB', 'value': 6415}, {'label': 'C', 'value': 5782}, {'label': 'D', 'value': 3013}, {'label': 'E', 'value': 2919}, {'label': 'F', 'value': 6320}, {'label': 'G', 'value': 2290}], [{'label': 'A', 'value': 2787}, {'label': 'BBBB', 'value': 6636}, {'label': 'C', 'value': 8877}, {'label': 'D', 'value': 7162}, {'label': 'E', 'value': 9008}, {'label': 'F', 'value': 6676}, {'label': 'G', 'value': 4436}], [{'label': 'A', 'value': 2814}, {'label': 'BBBB', 'value': 3602}, {'label': 'C', 'value': 1139}, {'label': 'D', 'value': 2279}, {'label': 'E', 'value': 1194}, {'label': 'F', 'value': 9630}, {'label': 'G', 'value': 8964}], [{'label': 'A', 'value': 8211}, {'label': 'BBBB', 'value': 9529}, {'label': 'C', 'value': 2484}, {'label': 'D', 'value': 7844}, {'label': 'E', 'value': 7529}, {'label': 'F', 'value': 5679}, {'label': 'G', 'value': 3525}], [{'label': 'A', 'value': 8698}, {'label': 'BBBB', 'value': 1736}, {'label': 'C', 'value': 3162}, {'label': 'D', 'value': 9818}, {'label': 'E', 'value': 7472}, {'label': 'F', 'value': 9502}, {'label': 'G', 'value': 5177}], [{'label': 'A', 'value': 2779}, {'label': 'BBBB', 'value': 6897}, {'label': 'C', 'value': 1608}, {'label': 'D', 'value': 1272}, {'label': 'E', 'value': 1042}, {'label': 'F', 'value': 7968}, {'label': 'G', 'value': 4854}], [{'label': 'A', 'value': 8126}, {'label': 'BBBB', 'value': 3699}, {'label': 'C', 'value': 2109}, {'label': 'D', 'value': 6044}, {'label': 'E', 'value': 5117}, {'label': 'F', 'value': 3670}, {'label': 'G', 'value': 6950}], [{'label': 'A', 'value': 3538}, {'label': 'BBBB', 'value': 8702}, {'label': 'C', 'value': 7390}, {'label': 'D', 'value': 8261}, {'label': 'E', 'value': 2497}, {'label': 'F', 'value': 7770}, {'label': 'G', 'value': 2910}], [{'label': 'A', 'value': 4153}, {'label': 'BBBB', 'value': 2670}, {'label': 'C', 'value': 5514}, {'label': 'D', 'value': 6070}, {'label': 'E', 'value': 8280}, {'label': 'F', 'value': 8334}, {'label': 'G', 'value': 9338}], [{'label': 'A', 'value': 2028}, {'label': 'BBBB', 'value': 6650}, {'label': 'C', 'value': 6672}, {'label': 'D', 'value': 6361}, {'label': 'E', 'value': 4163}, {'label': 'F', 'value': 9270}, {'label': 'G', 'value': 7209}]]
// const labelInfo = {
//   'A': {
//     'color': '#e68686',
//     'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/225px-Flag_of_South_Korea.svg.png'
//   },
//   'BBBB': {
//     'color': '#e6af86',
//     'img': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAMAAABThUXgAAAAeFBMVEXtHCcCT6L////wQUv//PzuJzHxSVLzYmrtHyr/+vr+7u/vOkT1foTvMDr95ObyVV31hYvyWWH82tz5t7r2jJL1hoz6wMP3naL4pqr96er94OH6xcj+9PXxUlv4qq/uKzX0b3b3lZr81dfzaXH7zdDwRU71e4L5tLhcZhK4AAAElElEQVR4nO2d63LiMAyFsyE3wiXhtkBpKaVsef83XEyaxI5lQOzOGKrz/eiU2Om4Z6JYkmUT/AI3E/gewDMBsRhALAYQiwHEYgCxGEAsBhCLAcRiALEYQCwGEIsBxGIAsRhALAYQiwHEYgCxGEAsBhCLAcRiALEYQCwGEItBEIKbgVgMIBYDiMUg6IGbCQAAAAAAAAAA3EM2SCZpOkkGme+RPDZZUs5eolOw3u+ffkTTWZlAMZKs2OZ1ZmN7rH/LtwX06hKXYy0NlKbah3EZ+x7dQxHPc02dMHqPI/1zPodcDan+VJ04BMHBvLLe+R7jgzD63U3GDoNg2L32e+R7nI9AsbYy14MgGFgX1xPfI/VPGVmyHNT1g3U5Gvoeq28+LE3CsFQNC6JhKduLWBGSKCuk7PDEyvd4fUI9V+G+attTbR9+x+uTktIjnFeNc7JR7HursN/tiu+VyR7ZGAmdE0e2z6CY1u1Tsnkt09+yfNGK5rVEvtBO3qnPMfvik9YiTOoOiaND6nPUfohpIwxf2i4vdI+xvKianuwM58Bhh/V0KYc4dyiRtH1cdphLe7SoaOZsY3qnsaNT6WvUfshcOiz1XkuXorJixIlDhvBN7/Xm6lX4GrcXtg4V1sYzkzlmTFkBdZZvBvffPdjkkuzwNM/1d/fenL4ac+aP5zwXHt/vuTU+W7Ck+XBWTWpv13t2SSq3fvb/x/SwfAcy0Zz77hn2qzun17v+FLImkcVb4GoXzfpy3vBafj1n5BAmmifxD5Ppk2EEfasbI73sQ0+sypkOC8PDnN60w6W3N26S48Onxv8d9m9Yhdi9mvfIyQB2xLrucsVWeCRHrKL7r19xuRI7ZyrHDIms3iWXq3audOS84Mml+Y1jVozJVSA5rkNGra5GjvfWO/FcSXJKyfVT53og9WQJCne+A2mTL1fnL6KzpECaqAiJnFHiiDBaSSkaYjrcuHtv7N5yJkOVVr7dCik7FJVWthcs3FZI2aGoBQvbhz9c6m0V496RYn1muousZixdmCVr3aJ4YYus1nyoe+TxMgy3uj/f9fglzYWKTmHIXmvq7dWV6R/t0t7oLK4wpFNytGgb6syVnuVauDoLITbeWk2yND62F2dNtGjYocBiNqNMsrFCM3PVZrl0O5ST99PQAuS6lm/Y8aiaLJdmtJLCwhattLuywhER1xyqabItihda2t1uGqiKblOycvL189xYJ3WkbhponU1VdBu7yvwql6suxhW7HaWRoGctCxool6vXyiqW8xa6sb0saKJcrvM0KSuAtlDT3CI7XpJKMYtVfLS8/vd+Nidv4dOxlUJnvMO230BtKKd30nWIsKFcYR9VQBqiUP/KonsIhg0OwWjpHK/SJV8IjJ0vYB7cY4CDe2z0I6G0h2olp16GhzpsbNqUNvSnsyEOG7tMdYxdgWPsAAAAAAAAAOCR8f2VUs8EvliNAcRiALEYQCwG+AJbBhCLAcRiALEYQCwGEIsBxGIAsRhALAYQiwHEYgCxGEAsBhCLAcRiALEYQCwGEIsBxGIAsRhALAYQiwHEYgCxGEAsBn8BD6OBoKGHPFgAAAAASUVORK5CYII='
//   },
//   'C': {
//     'color': '#dfe686',
//     'img': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAACWCAMAAAAfSh8xAAAAZlBMVEX///+8AC3ADznJM1f56OzSVXO+CTTdf5bvw87BEjz++/zmobLrssDfhZvjlKfwxtDkmqzQTm367fDtu8f34OXpqrnZboj99vjFIknLO17bd4/XZoH78PPUXXrHK1DDG0PhjaHORGVhMFMBAAACt0lEQVR4nO3cCXaqQBAFUAvQ4BAFcZ5i9r/JyFfzJSpj9amieHcF/U63dvVErwcAAAAAAAAAAAAAAADQLkESrb79zZdH3tfGj1dREkg3iVEw2fn0bLMfL6SbxuEw/n6R7s4/z6Ub2FDYH+TkSw36oXQjGwjjgnhX24l0Q2sKX/343gzWNvZjcCydL9Vv3V/r1KsUkMibSje5kkO/Yr5U3KK/1dmmRsDLBDmTbnhZUdEM8c4gkm56OZ8186U+pBtfxq5BQKKVdPOL7RsFJNpLByjSrAdTygfqtHFAorN0iDxLhoBEisvUxZAload22TjasgS8FOIj6ShvrJgCqp0zQraARCrrt1H55WCxk8ZxemYMSKRwLRVUXRDm8/QtpZoXM1k76UB/zXm78NKJB+lIf3wwByT6lI6UteapZh4N19KhMngK0qyldKiMclu/1cTSoR4FDgISadpC5VgWPtM067sYpKqG6Yh7Mrzy9BSnMycBNa0wmuyQ5tEz6dc5pSijLx3s18lRwpN0sF91zymKDKSD3S0cBSTSsumWOEuYSEe7cVF2X2nZGx47SziWjnbjpipNaalMXU34eqZ8+wntj1L7/zT2Zwv7M779qs1+5d2B1ZP9FbD9XQz7O1H2dxPt7wh3YFc/cDEjDlQd5Zs/XevACan9U277NxV6B/O3TdhvDOm7DG3/1pf9m3u8ty913hLmXGHoWVVk8N2CVncx8cb+TXau1whDNVtszyYsCbXsA7/EsVDUOFE8MP+yqwOv8zrwwrJZ+aZ+iF6Na7901nJeWMj8a/UOfHHgIqpa3gxb8hb/v3m1Ovyo6dp6WWH5Qnzbol9ghvUv8KRmxV9ROra1/+7Wy7yO3EbqNg3rOCRvvma2bNf8kC8Io13sn/59ke7kx7sotJQOAAAAAAAAAAAAAAAAuuEHEIYplcNWgA8AAAAASUVORK5CYII='
//   },
//   'D': {
//     'color': '#a6e686',
//     'img': 'https://png.pngtree.com/element_pic/00/16/09/3057ee81f935fd3.jpg'
//   },
//   'E': {
//     'color': '#86e6a4',
//     'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_Thailand.svg/225px-Flag_of_Thailand.svg.png'
//   },
//   'F': {
//     'color': '#86e6d5',
//     'img': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWYAAACNCAMAAACzDCDRAAAAkFBMVEWNGz3///+FACiIADCHAC6GACqMFjqJADKEACWEACOLEDeHAC+FACmKCjXw5OeGACzbwMfexsyta3vXusH79viBABvAkZyxc4LRsLjs3uKqZXa3f4zEmKLp2Nz17e+mW26VMEzLpK2eSV+ZPVbjz9SRI0S7iJShUGXOqbKbQVqgTGN/AA2taXrdxcq2fIqoXnEkFx/nAAAEo0lEQVR4nO2d25KqMBBFDYqioyjKKJ4BvOFtzlz+/+9OOsxD6swzvavYWX/gKmunOySdgdEiLXazZDgbcKKmWdifDvF8Mkb/ZgCqmoVme5kuF2yq1TVb6s3uSpYfCM2CzY8hUX6gNFvy7HaJSPIDqFmw+TGOhv03DdYspI9n7z2jHRuTbc/9Xw2xiu1CmMQMCyFOsY3lCU1ZB3LcbI/JcoH+8XoAFNukGBGVzA5lxTYpBhFLUngoKs6b7WVO0o78j5rk1f31dUSpWFDTLL31kaW3/oWeZqHerBeM0QyoNKryHlG0JD76mo3Lj+t0xPSnhmgW6mI9iiYsqmGahap8n8YUiyJUsyX/fDvG/ReN1ixkl957RivOV1/XZe8tYzU35TkO2dwp6ePPIqIpnyGK89XbcfrCUswJ+o6r8sx37EhXcVp8LHl6Eg89xTYpyDpsDzXLq0PYb9bBpnLCUb/9QlOzYawxWpQ1C1wVcwtAs8DT/7WANJt2NyNiyQ+cZsHmx4QiP7Cahaa8998zWrJl/wj7zR2TFuuYITWAivPP2zUh6b5Rjm1HOCc6rYFQnBYfM7J9Om3FNimOEUlSeKg6rsr7iCgpPNQU205knHAlhYeeZjmnz9Jb/0JNs7B/fIdBDzqEQQ9a5JuvMc2NwBaEZmF/OkRE+YHSLDQ3mvxAajbtPcEkDHrQIH0ce+8Z7VguZZ7REroH65hm4hFOcRvLJGUdyDFbkwJQTFYyO5QV26RY0CSFh6bjZnukSgoPNcfZ+99w8FYBGaLI+mfWH/TAU8T56GoW9owfBPU1m59BMVSftyGahbpYL3gOa8A0C1V5jjgOk0M1Gzfo4RoGPagQBj10Tr76GoR/c7c05TNkc7fQXDtxQBTL9e1QN3eLreKWHEnhoas4LT7oLrg69BS769pUSeGhZjkLgx6UqMon64azpmbjkmMQBj2oYCvmJds6CNAsNGTju0CajdvN4BkUg9Ms0AyKwWoWmvKOltA9aMkmDHpQoC7WM4bUACrOM9d999/xADjo4XSfEp3WQCi2STEke2RGW3H75AnRS4Etqo5tUvA94ONQU5xKTcGVFB5qmm0gXykPgzrUNAv702HCduukRVWzoX0CU1uzUG92Y7KYRmgWbH7EREUHSrOQ3eRmFdqACkjNxuXHMAx6UCEtwkZo92TbJ1pC92AV24XwhWIhxCmWQQ80ZR1GsTQpVE+bAxzTjITxUFZsk4JyA0nTMdtIGA81xzLo4YVSsaCm2V3UZumtf6GnWaiL3YQxmhFXfBg/COprFmRQzIhpMcRoNu7bINEQZ5hmweYHyaAYqGbT1h8EdR5as5A9e+8ZrVjewAyDHrql2bJcFIQpTh/fc559OojifPU2o7lE5dB33JTPhCMpPHQVpwXTSBgPPcU13UgYDzXL2WEaBj2oUJXPmG78ToumZvMzTIqqxmhR1iykjz9DtnUQoFlgq+pAmo3bzRjT9Cg4zYLNj5giP7Cahaa8998zWrKRw15hv7lj0jDooWt+HjLov+MBdNDDkuNrqwOhuC7oHpnRVuxO0lGdhHGoOq5Oh4QoKTzUFNuagvOUovAPLf6Al2hUtMQAAAAASUVORK5CYII='
//   },
//   'G': {
//     'color': '#86a7e6',
//     'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/225px-Flag_of_Saudi_Arabia.svg.png'
//   },
//   'H': {
//     'color': '#9e86e6',
//     'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/225px-Flag_of_Saudi_Arabia.svg.png'
//   },
//   'I': {
//     'color': '#c686e6',
//     'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/225px-Flag_of_Saudi_Arabia.svg.png'
//   },
//   'J': {
//     'color': '#e686da',
//     'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/225px-Flag_of_Saudi_Arabia.svg.png'
//   },
// }

let instance = null

const elements = {}
const elementList = []

const createElement = (data) => {
  if (data.value !== '-') {
    data.value = Number(Number(data.value).toFixed(2))
    elements[data.label] = {
      value: data.value,
      node: createNode(data)
    }
    const node = elements[data.label].node
    instance.element.appendChild(node)
    instance.add([node])
  }
}

function getRandomColor () {
  var letters = '0123456789ABCDEF'
  var color = '#'
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)]
  }
  return color
}

function numberWithCommas (x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}

const createNode = (data) => {
  var div = document.createElement('div')
  let color, img
  try {
    color = labelInfo[data.label].color
    img = labelInfo[data.label].img
  } catch (err) {
    console.log(data.label)
    color = getRandomColor()
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

  elementList.push(div.firstChild)
  // Change this to div.childNodes to support multiple top-level nodes
  return div.firstChild
}

const getNodeValue = (node) => {
  return Number(node.children[3].innerHTML) - 77
}

const setNodeValue = (node, value) => {
  node.children[3].innerHTML = value
}

const top = 15
const setWidth = () => {
  const newList = elementList.concat().sort(function(n1, n2) {
    return getNodeValue(n2) - getNodeValue(n1)
  })
  const max = getNodeValue(newList[0])
  const maxWidth = 1500
  for (let i = 0; i < newList.length; i++) {
    const element = newList[i]
    if (i < top) {
      const width = ((getNodeValue(element) / max) * maxWidth).toFixed(2)
      element.children[1].style.width = width + 'px'
      if (element.style.display !== 'table') {
        element.style.display = 'table'
        // instance.element.appendChild(element)
        // instance.add([element])
      }
    } else {
      if (element.style.opacity === 0) {
        element.style.display = 'none'
      } else if (element.style.display !== 'none') {
        // element.style.display = 'none'
        element.style.opacity = 0
        // if (element.parentNode != null) instance.remove([element])
      }
    }
  }
  // for (const label in elements) {
  //   if (max < elements[label].value) max = elements[label].value
  // }
  // for (const label in elements) {
  //   const width = ((elements[label].value / max) * maxWidth).toFixed(2)
  //   elements[label].node.children[1].style.width = width + 'px'
  // }
}

export default {
  name: 'MyShuffle',
  mounted () {
    instance = new Shuffle(document.getElementById('container'), {
      itemSelector: '.item',
      speed: 1000
    })

    // Initial value
    const years = []
    for (let i = 1999; i <= 2016; i++) years.push(i)
    document.getElementById('year').textContent = years[0]
    for (const i in data[0]) {
      const curData = data[0][i]
      createElement(curData)
    }

    setWidth()
    instance.sort({
      by: (element) => {
        return getNodeValue(element)
      },
      reverse: true
    })
    const intervalRange = 8 * 1000
    let index = 1
    const interval = setInterval(() => {
      if (index < data.length) {
        document.getElementById('year').textContent = years[index]
        const fromTweening = {}
        const toTweening = {}
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
          if (curData.value !== '-') {
            fromTweening[curData.label] = prevData.value
            toTweening[curData.label] = curData.value

            // const tweening = {value: prevData.value}
            // new TWEEN.Tween(tweening)
            //   .to({value: curData.value}, intervalRange * 0.99)
            //   // .easing(TWEEN.Easing.Quadratic.Out)
            //   // .easing(TWEEN.Easing.Quadratic.InOut)
            //   .easing(TWEEN.Easing.Linear.None)
            //   .onUpdate(() => {
            //     // if (curData.label === 'A') {
            //     //   console.log(Number(tweening.value.toFixed(0)) - Number(prevData.value))
            //     // }
            //     prevData.value = Number(tweening.value.toFixed(2))
            //     setNodeValue(prevData.node, prevData.value)
            //     setWidth()
            //   })
            //   .start()
          }
        }
        new TWEEN.Tween(fromTweening)
          .to(toTweening, intervalRange * 0.99)
          .easing(TWEEN.Easing.Linear.None)
          .onUpdate(() => {
            for (const label in fromTweening) {
              const value = Number(fromTweening[label].toFixed(2))
              elements[label].value = value
              setNodeValue(elements[label].node, value)
            }
            setWidth()
          })
          .start()
      } else {
        clearInterval(interval)
      }
      index++
    }, intervalRange)

    setInterval(() => {
      instance.sort({
        by: (element) => {
          return getNodeValue(element)
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
