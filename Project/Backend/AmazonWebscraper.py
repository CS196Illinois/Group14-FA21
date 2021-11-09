from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/search/<keyword>', methods=['GET'])
def get_data(keyword):
    url = "https://www.amazon.com/s?k=" + keyword
    return _webscrapping(url)

def _webscrapping(url):
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15'}
    sauce =  urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce, 'html.parser')

    # Extract and records data of a single item
    def extract_price(item):
        try :
            price_parent = item.find('span' , 'a-price')
            price = price_parent.find('span', 'a-offscreen').text
        except AttributeError:
            return
        return price

    # Extract and records title of a single item
    def extract_url(item):
        try :
            # title
            atag = item.h2.a
            url = "https://www.amazon.com" + atag.get('href')
        except AttributeError:
            return
        return url

    # Extract and records rating of a single item
    def extract_rating(item):
        try :
            # rating
            rating = item.i.text
        except AttributeError:
            return
        return rating

    # Array of prices as floats
    def makeArrayofItemsPrice():
        records = []
        results = soup.find_all('div',{'data-component-type': 's-search-result'})
        for item in results:
            record = extract_price(item)
            if(record):
                records.append(record)
        records_float = []
        for item in records:
            records_float.append(float(item[1:]))
        return records_float

    # Array of all titles 
    def makeArrayofItemsUrl():
        results = soup.find_all('div',{'data-component-type': 's-search-result'})
        urls = []
        for item in results:
            url = extract_url(item)
            if(url):
                url.append(urls)
        return urls
    
    # Array of all ratings 
    def makeArrayofItemsRating():
        results = soup.find_all('div',{'data-component-type': 's-search-result'})
        ratings = []
        for item in results:
            rating = extract_rating(item)
            if(rating):
                ratings.append(rating)
        return ratings

    # Return cheapest five prices from list of prices passed in as parameter
    def cheapest_five():
        urls = makeArrayofItemsUrl()
        prices = makeArrayofItemsPrice()
        ratings = makeArrayofItemsRating()
        df = pd.DataFrame(urls)
        df["price"] = prices
        df["rating"] = ratings
        df.rename(columns = {0 : "urls", "price" : "price",  "rating" : "rating"}, inplace=True)
        df = df.sort_values(by='price')
        d = df.head(5).to_dict()
        return d
    return cheapest_five()

if __name__ == '__main__':
    app.run(debug=True)
