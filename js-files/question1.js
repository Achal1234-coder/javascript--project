var dataSet;
var arr = new Array();
var questionNo = 1;
var category;
var time;
showSlides();


function stop(){
    var bt = document.getElementById("button");
    if(bt.innerHTML === "Stop"){
        bt.innerHTML = "Start";
        clearTimeout(time);

    }
    else{
        bt.innerHTML = "Stop";
        late("Start");
    }
}


function showSlides(){
    let url;
    let yText;
    let xText;
    let pointFormat;
    let graphName;

    if(questionNo === 1){
        url = "question1.json";
        graphName = "Total runs scored by team";
        yText = "Teams Run"
        xText = "Teams"
        pointFormat = "{point.y:.1f} Runs"
    }

    else if(questionNo === 2){
        url = "question2.json";
        graphName = "Top 20 batsman for Royal Challengers Bangalore"
        yText = "Player Runs"
        xText = "Players"
        pointFormat = "{point.y:.1f} Runs"
    }

    else if(questionNo === 3){
        url = "question3.json";
        graphName = "Foreign umpire analysis"
        yText = "No of umpires"
        xText = "Countries"
        pointFormat = "{point.y:.1f} Umpires"

    }

    else{
        url = "question4.json";
        graphName = "Stacked chart of matches played by team by season"
        yText = "No of Matches"
        xText = "Years"
    }

    questionNo++;
    if(questionNo === 5){
        questionNo = 1;
    }

    fetch("json/" + url)
    .then(respons => respons.json())
    .then(data => {
        dataSet = data;
        arr.length = 0;

        calculateArray();

        if(questionNo === 1){
            plotGraph2(graphName, yText, xText);
        }
        else{
            plotGraph1(graphName,yText, xText, pointFormat);
        }

        late();
    })

}

function late(value = "Stop"){
    if(value === "Start"){
        time = setTimeout(showSlides, 200);
    }
    else{
        time = setTimeout(showSlides, 5000);
    }
}


function calculateArray(){


    for (const item of Object.entries(dataSet)) {

        if(questionNo !== 1){
            arr.push([item[0], item[1]]);
        }

        else{

            category = Object.keys(dataSet)
            list_of_teams = ['RCB', 'MI', 'CSK', 'DD', 'KKR', 'k XI P',
                         'RR', 'SH', 'GL', 'RPS', 'KTK', 'PW', 'DC'];

            if(arr.length === 0){

                for(let team of list_of_teams){
                    let obj = {};
                    obj['name'] = team;
                    obj['data'] = [];
                    arr.push(obj);
                }
            }

            index = 0;
            for(let team of list_of_teams){

                if(team in item[1]){
                    arr[index]['data'].push(item[1][team])
                }

                else{
                    arr[index]['data'].push(0)
                }
                index++;
            }

        }

    }

}

function plotGraph1(text, yText, xText, pointFormat){ Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: text
    },
    xAxis: {
        type: 'category',
        title: {
            text: xText
        },
        labels: {
            rotation: -90,
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: yText
        }
    },
    legend: {
        enabled: false
    },
    tooltip: {
        pointFormat: pointFormat
    },
    series: [{
        data: arr,

    dataLabels: {
        enabled: true,
        rotation: -90,
        color: '#FFFFFF',
        align: 'right',
        format: '{point.y:.1f}', // one decimal
        y: 10, // 10 pixels down from the top
        style: {
            fontSize: '13px',
            fontFamily: 'Verdana, sans-serif'
        }
    }
}]
});}

function plotGraph2(text, yText, xText){Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: text
    },
    xAxis: {
        categories: category,
        title: {
            text: xText
        }
    },
    yAxis: {
        allowDecimals: false,
        min: 0,
        title: {
            text: yText
        },
        stackLabels: {
            enabled: true

        }


    },
    legend: {
        reversed: true
    },
    plotOptions: {
        series: {
            stacking: 'normal',
            dataLabels: {
                "enabled": "true"
            }

        }
    },
    series: arr
});}
