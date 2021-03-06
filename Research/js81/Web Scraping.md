# What I found
### LXML
- Fast at scraping large documents
- Well documented
- Easy file manipulation
- Has a soupparser so you can use beautiful soup’s functionality if needed
  
### Scrappy
- Open source framework
- CPU and memory efficient
- Best for big scale web scraping
- Well structured → more flexible and adaptable
- Dont use if use scraping a few webpages, will over complicate things

### Beautiful Soup
- Good for beginners
- Best to use if documents are not structured
- Not good for big for big projects because not flexible and hard to maintain as project size increases
- *Beautiful Soup can only parse data and not request so normally used along side the Requests library*

### Requests
- Good for starting out
- Simple and dont need alot of practice
- Very well written documentation
- Dont use if webpage jas JS content → wont parse the correct information

### Urlib
- Offers functionality to deal with and open URL’s
- Bit more complicated that Request but you get more control 

### Selenium
- Good for beginners but also powerful
- Good for a few webpages and the information you need is in JS 
- High CPU usage not good for big projects

### List of Links: 
- Overview of libraries: https://towardsdatascience.com/choose-the-best-python-web-scraping-library-for-your-application-91a68bc81c4f
- LXML: https://stackabuse.com/introduction-to-the-python-lxml-library/
- LXML vs Beautiful Soup: https://stackoverflow.com/questions/4967103/beautifulsoup-and-lxml-html-what-to-prefer
- Basic flask tutorial: https://www.youtube.com/watch?v=Z1RJmh_OqeA
- Flask Tutorial to Create an Endpoint: https://www.youtube.com/watch?v=s_ht4AKnWZg 

# How this can be used in the context of the project
Overall I think that the top three web scraping libraries we could use would be 1. LXML 2. Scrappy 3. Beautiful Soup/Requests. LXML is fast at scraping 
large documents which I think can be useful since we might be scraping various websites. It also has a soupparser so we can use Beautiful Soup's functionality
if needed. Scrappy is also good for big scale webscraping and is memory efficient. Beautiful Soup/Requests is good for beginners and might be easier for us to learn.

