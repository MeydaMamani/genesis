$("#searchKids").click();
$("#searchPreg").click();

var options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: true
        },
        datalabels: {
            formatter: (value, ctx) => {
                let percentage = value + "%";
                return percentage;
            },
            color: 'black',
            anchor: 'end',
            align: 'top',
            offset: 1,
            font: {
                size: 10,
                weight: '#656565'
            },
        }
    },
    scales: {
        y: {
            beginAtZero: true,
            max: 100,
        }
    },
};