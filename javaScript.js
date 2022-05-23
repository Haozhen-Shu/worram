// import fetch from  'node-fetch';
// const fetch = require('node-fetch');
let url = 'https://top-100-example.s3.amazonaws.com/t100_2021_full.json'
let response = async () => {
    let data = await fetch(url).then(response =>response.json())
    console.log(data)
}



// "id", "winery_full", "wine_full", "color", "price"
let arr  = []
for (let i = 0; i < data.length; i++) {
    let obj = new Object
}