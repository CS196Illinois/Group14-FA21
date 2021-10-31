//function that will make the call to backend and update the view
async function handleSearch(event) {
    const productName = document.getElementById("product-name").value;
    const loading = document.getElementById("loading")
    const errors = document.getElementById("errors");
    loading.textContent = "loading..."
    errors.textContent = "";
    try {
        const response = await fetch(`http://127.0.0.1:5000/search/${productName}`);
        const jsonResponse = await response.json();
        loading.textContent = "";
        document.getElementById("first").textContent = jsonResponse.name['0'];
        document.getElementById("second").textContent = jsonResponse.name['1'];
        document.getElementById("third").textContent = jsonResponse.name['2'];
        document.getElementById("fourth").textContent = jsonResponse.name['4'];
        document.getElementById("fifth").textContent = jsonResponse.name['7'];
    }
    catch (error) {
        loading.textContent = "";
        errors.textContent = "We have no data for the product you have requested.";
    }
}

//adds an event listener to the button that will call the handleSearch function
var b = document.getElementById("bttn");
b.addEventListener("click", handleSearch, false);
