<template>
  
    <g-gantt-chart
      :chart-start="myChartStart"
      :chart-end="myChartEnd"
      precision="months"
    >
      <g-gantt-row
        v-for="row in rows"
        precision="day"
        :key="row.label"
        :label="row.label"
        :bars="row.bars"
        bar-start="myStart"
        bar-end="myEnd"
      />
    </g-gantt-chart>
  
  </template>
  
  <script>
  
  import {GGanttChart, GGanttRow} from 'vue-ganttastic'
  
  export default {
  
    components:{
      GGanttChart,
      GGanttRow
    },
  
    data(){
      return {
        myChartStart: "2023-03-01 00:00",
        myChartEnd: "2023-03-03 00:00",
        rows: [
          {
            label: "My row #1",
            bars: [
              {
                myStart: "2023-03-01 12:10",
                myEnd: "2023-03-01 16:35"
              }
            ]
          },
          {
            label: "My row #2",
            bars: [
              {
                myStart: "2023-02-02 01:00",
                myEnd: "2023-03-01 12:00"
              },
              {
                myStart: "2023-03-02 13:00",
                myEnd: "2023-03-10 22:00"
              }
            ]
          }
        ]
      }
    }
  
  }
  </script>