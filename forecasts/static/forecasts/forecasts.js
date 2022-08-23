accounts = fetch('/accounts/api/get-checkpoints/', {
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

const DATA_COUNT = 7;
const NUMBER_CFG = {count: DATA_COUNT, min: 0, max: 100};
const data = [
  {x: 'Jan', net: 100, cogs: 50, gm: 50}, 
  {x: 'Feb', net: 120, cogs: 55, gm: 75}
];
const cfg = {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb'],
        datasets: [{
            label: 'Net sales',
            data: data,
            parsing: {
                yAxisKey: 'net'
            }
        }, {
            label: 'Cost of goods sold',
            data: data,
            parsing: {
                yAxisKey: 'cogs'
            }
        }, {
            label: 'Gross margin',
            data: data,
            parsing: {
                yAxisKey: 'gm'
            }
        }]
    },
};
    
const myChart = new Chart(
    document.getElementById('myChart'),
    cfg
  );


