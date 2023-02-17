url = 'https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json'

d3.json(url).then(function(data){
    console.log(data);

    let title = data.samples[0].otu_labels[0].split(';')
    console.log(title);
    d3.select('h1').text(title[3]);

    for(i=0;i<title.length;i++){
        d3.select('ul').append('li').text(title[i]);
    }

});

// function doStuff(){
//     console.log('getting name...');
//     let userinfo = document.getElementById('username').value;
//     console.log(`Hello, ${userinfo}`);
//     const request = new XMLHttpRequest();
//     request.open('POST', `/ProcessUserinfo/${JSON.stringify(userinfo)}`);
//     request.send();
// }

function getData(){
    url = 'http://127.0.0.1:5000/accidents'
    fetch(url).then(response => response.json())
    .then(json => {console.log(json);
    document.getElementById('test').innerHTML = JSON.stringify(json)});
}

function doStuff(){
    let value = document.getElementById('year').value;
    let url = `http://127.0.0.1:5000/api/v1.0/${value}`
    fetch(url).then(response => response.json())
    .then(json => {console.log(json);
    document.getElementById('test').innerHTML = JSON.stringify(json)});
}