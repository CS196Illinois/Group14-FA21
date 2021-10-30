from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

app = Flask(__name__)

@app.route('/search/', methods=['GET'])
def get_data():
    search_req=request.args.get('q')
    return _webscrapping(search_req)

    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15'}
    sauce =  urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce, 'html.parser')

    # Extract and records data of a single item
    def extract_price(item):
        try :
            price_parent = item.find('span' , 'product__price font__sixteen color__text-red')
            price = price_parent.find('span', 'sr-only').text
        except AttributeError:
            try :
                price_parent = item.find('span' , 'product__price font__sixteen wag-inline-txt')
                price = price_parent.find('span', 'sr-only').text
            except AttributeError:
                return
        return price

    # Extract and records title of a single item
    def extract_title(item):
        try :
            # price
            title_parent = item.find('div', class_= 'product__title font__fourteen')
            title = title_parent.find('strong', class_='description').text.strip()
        except AttributeError:
            return
        return title

    # Array of prices as floats
    def makeArrayofItemsPrice():
        records = []
        results = soup.find_all('div',{'class': 'item card card__product'})
        for item in results:
            record = extract_price(item)
            if(record):
                records.append(record)
        records_float = []
        for item in records:
            records_float.append(float(item[1:]))
        return records_float

    # Array of all titles 
    def makeArrayofItemsName():
        results = soup.find_all('div',{'class': 'item card card__product'})
        titles = []
        for item in results:
            title = extract_title(item)
            if(title):
                titles.append(title)
        return titles

    # Return cheapest five prices from list of prices passed in as parameter
    def cheapest_five():
        titles = makeArrayofItemsName()
        prices = makeArrayofItemsPrice()
        df = pd.DataFrame(titles)
        df["price"] = prices
        df.rename(columns = {0 : "name", "price" : "price"}, inplace=True)
        df = df.sort_values(by='price')
        return df.head(5)
    return cheapest_five()

if __name__ == '__main__':
    app.run(debug=True)
