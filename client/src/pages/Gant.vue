<template>
  
    <g-gantt-chart
      :chart-start="myChartStart"
      :chart-end="myChartEnd"
    >
      <g-gantt-row
        v-for="row in rows"
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
        myChartStart: "2020-03-01 00:00",
        myChartEnd: "2020-03-03 00:00",
        rows: [
          {
            label: "My row #1",
            bars: [
              {
                myStart: "2020-03-01 12:10",
                myEnd: "2020-03-01 16:35"
              }
            ]
          },
          {
            label: "My row #2",
            bars: [
              {
                myStart: "2020-03-02 01:00",
                myEnd: "2020-03-02 12:00"
              },
              {
                myStart: "2020-03-02 13:00",
                myEnd: "2020-03-02 22:00"
              }
            ]
          }
        ]
      }
    }
  
  
  }
  </script>