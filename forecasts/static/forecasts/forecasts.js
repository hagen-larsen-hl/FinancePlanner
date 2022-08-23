const DATA_COUNT = 7;
const NUMBER_CFG = {count: DATA_COUNT, min: 0, max: 100};

accounts = fetch('/accounts/get/', {
    method: 'GET',
    credentials: 'same-origin',
    headers: {
        'Content-Type': 'application/json',
        "Accept": "application/json"
        },
        }).then(response => response.json()).then(data => {
            console.log(data);
            return data;
        });
        
const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
const data = {
  labels: labels,
  datasets: [
    {
      label: 'My First dataset',
      data: [50, 100, 150, 200, 250, 300, 350],
      borderColor: '#00bcd4',
      backgroundColor: '00bcd4',
      fill: true
    },
    {
      label: 'My Second dataset',
      data: [50, 100, 150, 200, 250, 300, 350],
      borderColor: '#ffc107',
      backgroundColor: '#ffc107',
      fill: true
    },
    {
      label: 'My Third dataset',
      data: [50, 100, 150, 200, 250, 300, 350],
      borderColor: '#ff5722',
      backgroundColor: '#ff5722',
      fill: true
    },
    {
      label: 'My Fourth dataset',
      data: [50, 100, 150, 200, 250, 300, 350],
      borderColor: '#03a9f4',
      backgroundColor: '#03a9f4',
      fill: true
    }
  ]
};const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: (ctx) => 'Chart.js Line Chart - stacked=' + ctx.chart.options.scales.y.stacked
        },
        tooltip: {
          mode: 'index'
        },
      },
      interaction: {
        mode: 'nearest',
        axis: 'x',
        intersect: false
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Month'
          }
        },
        y: {
          stacked: true,
          title: {
            display: true,
            text: 'Value'
          }
        }
      }
    }
  };
 

const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );


