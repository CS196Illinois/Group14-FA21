//this event is fired when the user puts keyword into search bar.
chrome.omnibox.onInputEntered.addListener(async(text) => {
    openWalgreensURLOnCurrentTab(text);
});

//opens up amazon link with the search as the text input
function openWalgreensURLOnCurrentTab(text) {
    var walgreensURL = 'https://www.walgreens.com/search/results.jsp?Ntt=' + text;
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var tab = tabs[0];
        chrome.tabs.update(tab.id, {url: walgreensURL});
    });
    console.log("url:" + walgreensURL);
}

