import axios from 'axios';
const axios = require('axios').default;
const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const first = document.querySelector(".first");
const second = document.querySelector(".second");
const third = document.querySelector(".third");
const fourth = document.querySelector(".fourth");
const fifth = document.querySelector(".fifth");
const results = document.querySelector(".result-container");
results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";

const form = document.querySelector(".form-data");
const product =document.querySelector(".product-name");

const find5Links = async productName => {
    loading.style.display = "block";
    loading.textContent = "loading..."
    errors.textContent = "";
    try {
        const response = await axios.get(`localhost:3000/multi/${productName}`);
        results.style.display = "block";
        loading.style.display = "none";
        loading.textContent = "";
        first.textContent = response.data.first.value;
        second.textContent = response.data.second.value;
        third.textContent = response.data.third.value;
        fourth.textContent = response.data.fourth.value;
        fifth.textContent = response.data.fifth.value;
        results.style.display = "block";
    }
    catch (error) {
        loading.style.display = "none";
        results.style.display = "none";
        errors.textContent = "We have no data for the product you have requested.";
    }
};

const handleSubmit = async e => {
    e.preventDefault();
    find5Links(product.value);
    console.log("product name: " + product.value);
};

form.addEventListener("submit", e => handleSubmit(e));