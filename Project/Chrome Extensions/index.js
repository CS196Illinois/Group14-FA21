//function that will make the call to backend and update the view
async function handleSearch(event) {
    const productName = document.getElementById("product-name").textContent;
    const loading = document.getElementById("loading")
    const errors = document.getElementById("errors");
    loading.textContent = "loading..."
    errors.textContent = "";
    try {
        const response = await fetch(`localhost:3000/multi/${productName}`);
        const jsonResponse = await response.json();
        loading.textContent = "";
        document.getElementById("first").textContent = "first link";
        document.getElementById("second").textContent = "second link";
        document.getElementById("third").textContent = "third link";
        document.getElementById("fourth").textContent = "fourth link";
        document.getElementById("fifth").textContent = "fifth link";
    }
    catch (error) {
        loading.textContent = "";
        errors.textContent = "We have no data for the product you have requested.";
    }
}

//adds an event listener to the button that will call the handleSearch function
var b = document.getElementById("bttn");
b.addEventListener("click", handleSearch, false);
