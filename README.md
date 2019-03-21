## Dynamic Chart

Draw dynamic bar chart with time series data

### Samples

🎥 [link](https://www.youtube.com/watch?v=8riIpxxV0s0&t=8s)

or

```bash
npm install
npm start
```

visit http://localhost:8080

### Usage

```html
<template>
	<div>
        <dynamic-chart
                       :stats = [
                            [{label: 'A', number: 1}, {label: 'B', value: 2}],
                            [{label: 'A', number: 3}, {label: 'B', value: 1}],
                        ]
                       :labelInfo = {
                            'A': {img: 'image-url'}
                        }
                       :date = ['2019-03-01', '2019-03-02']>
    	</dynamic-chart>
    </div>
</template>
<script>
	import dynamicChart from './DynamicChart'
</script>
```

### Props

| Name           | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `interval`     | duration time of each date (default: 2000)                   |
| `limit`        | number of row to show (default: 15)                          |
| `shuffleSpeed` | shuffle speed, less means faster (default: 1000)             |
| `fixed`        | formats number using fixed-point notation (default: 0)       |
| `scale`        | minimum scale value (default: 500000000)                     |
| `maximum`      | if you want get the width of 1st row keep changing, give maximum value of total stats. Otherwise, the width of 1st row does not change (default: 0) |
| `dynamic`      | make chart not begin with 0, affected by min row value (default: false) |
| `unit`         | unit value follows after row value (default: '')             |

### Datasource

- https://databank.worldbank.org
- https://datacatalog.worldbank.org/public-licenses#cc-by
- Licensed under Creative Commons: By Attribution 4.0 License [link](https://creativecommons.org/licenses/by/4.0/)