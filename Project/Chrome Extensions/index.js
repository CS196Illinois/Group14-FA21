//function that will make the call to backend and update the view
async function handleSearch(event) {
    //get all the elements
    const productName = document.getElementById("product-name").value;
    const loading = document.getElementById("loading")
    const errors = document.getElementById("errors");
    const first = document.getElementById("first");
    const second = document.getElementById("second");
    const third = document.getElementById("third");
    const fourth = document.getElementById("fourth");
    const fifth = document.getElementById("fifth");
    //reset the results after every search
    loading.textContent = "loading..."
    errors.textContent = "";
    first.textContent = "";
    second.textContent = "";
    third.textContent = "";
    fourth.textContent = "";
    fifth.textContent = "";
    try {
        const response = await fetch(`http://127.0.0.1:5000/search/${productName}`);
        const jsonResponse = await response.json();
        loading.textContent = "";
        first.textContent = jsonResponse.name['0'];
        second.textContent = jsonResponse.name['1'];
        third.textContent = jsonResponse.name['2'];
        fourth.textContent = jsonResponse.name['4'];
        fifth.textContent = jsonResponse.name['7'];
    }
    catch (error) {
        loading.textContent = "";
        errors.textContent = "\r\nWe have no data for the product you have requested.";
    }
}

//adds an event listener to the button that will call the handleSearch function
var b = document.getElementById("bttn");
b.addEventListener("click", handleSearch, false);
