//import axios from 'axios';
//const axios = require('axios').default;
const errors = document.getElementById("errors");
const loading = document.getElementById("loading");
const first = document.getElementById("first");
const second = document.getElementById("second");
const third = document.getElementById("third");
const fourth = document.getElementById("fourth");
const fifth = document.getElementById("fifth");

// could change errors.value and loading.value to empty here

const productName = document.getElementById("product-name").value;

const find5Links = async productName => {
    loading.value = "loading..."
    errors.value = "";
    try {
        //const response = await axios.get(`localhost:3000/multi/${productName}`);
        loading.value = "";
        first.value = "test";
        second.value = "hi"
        third.value = "random"
        fourth.value = "hello"
        fifth.value = "bye bye"
    }
    catch (error) {
        loading.value = "";
        errors.value = "We have no data for the product you have requested.";
    }
};

const handleSubmit = async e => {
    e.preventDefault();
    find5Links(productName);
    console.log("product name: " + productName);
};

function handleSearch() {
    const productName = document.getElementById("product-name").value;
    document.getElementById("first").value = "test";
    document.getElementById("second").value = "hi";
    document.getElementById("third").value = "random";
    document.getElementById("fourth").value = "hello";
    document.getElementById("fifth").value = "bye bye";
}

//<script src="index.js" type = "text/javascript" /></script>