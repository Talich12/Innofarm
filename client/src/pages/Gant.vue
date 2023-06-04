<template>
  <div>
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
  </div>
  
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
            label: "Обработка",
            bars: [
              {
                myStart: "2020-03-01 12:10",
                myEnd: "2020-03-02 16:35"
              }
            ]
          },
          {
            label: "Калибровка",
            bars: [
              {
                myStart: "2020-02-02 01:00",
                myEnd: "20230-03-01 12:00"
              },
              {
                myStart: "2020-03-02 13:00",
                myEnd: "2020-03-10 22:00"
              }
            ]
            },
          {
            label: "Фиксация",
            bars: [
              {
                myStart: "2020-03-01 11:00",
                myEnd: "20230-03-01 12:00"
              }
            ]
          }
        ]
      }
    }
  
  
  }
  </script>

  <style>
  .g-gantt-row-label {
    min-width: 100px;
  }
</style>