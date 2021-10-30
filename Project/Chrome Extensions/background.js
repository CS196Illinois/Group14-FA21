//this event is fired when the user puts keyword into search bar.
chrome.omnibox.onInputEntered.addListener(async(text) => {
    openAmazonURLOnCurrentTab(text);

});

//opens up amazon link with the search as the text input
function openAmazonURLOnCurrentTab(text) {
    var amazonURL = 'https://www.amazon.com/s?k=' + text;
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var tab = tabs[0];
        chrome.tabs.update(tab.id, {url: amazonURL});
    });
    console.log("url:" + amazonURL);
}

//currently this opens up an html with 5 random links
//but in future this should hold the top 5 links
/*
function openTop5Links(text) {
    const productName = text;
    try {
        const response = await fetch(`https://127.0.0.1:3000/multi/${productName}`);
        const jsonResponse = await response.json();
        chrome.tabs.create({url: 'top5.html'});
    }
    catch (error) {
        chrome.tabs.create({url: 'apple.com'});
    }
}
*/

