// 基于准备好的dom，初始化echarts实例
function assetPie(arr){
  var myChart = echarts.init(document.getElementById('main'));

  // 指定图表的配置项和数据
  var option = {
      legend: {},
      tooltip: {},
      dataset: {
          source: arr
      },
      xAxis: {type: 'category'},
      yAxis: {},
      // Declare several bar series, each will be mapped
      // to a column of dataset.source by default.
      series: [
          // {type: 'bar'},
          // {type: 'bar'},
          // {type: 'bar'},
          // {type: 'bar'},
          ]
  };
  for (let i = 1; i < arr.length; i++) {
      console.log(i);
      option['series'].push({type: 'bar'})
      console.log(option['series'])
  }

       console.log(option['series'])

  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option);
}