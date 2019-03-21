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

```vue
<template>
	<div>
        <dynamic-chart
                       :stats = {{stat}}
                       :labelInfo = {{labelInfo}}
                       :date = {{date}}
                       :interval = {{interval}}
                       :limit = {{limit}}>
    	</dynamic-chart>
    </div>
</template>
<script>
	import dynamicChart from './DynamicChart'
</script>
```



