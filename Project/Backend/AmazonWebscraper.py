from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json


app = Flask(__name__)

@app.route('/search/<keyword>', methods=['GET'])
def get_data(keyword):
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_2"
    keyword = keyword.replace(' ', "+")

    # add term to query url
    url = template.format(keyword)

    #add page query placeholder
    url += '&page{}'
    return _webscrapping(url)

def _webscrapping(url):
    def extract_record(item):
        #description and url
        atag = item.h2.a
        description = atag.text.strip()
        url = 'https://www.amazon.com' + atag.get('href')

        try:
            #price
            price_parent = item.find('span',  'a-price')
            price = price_parent.find('span', 'a-offscreen').text
            price = price.replace("$","")
            price = price.replace(",","")
            price = float(price)
        except AttributeError:
            return

        
        result = (description, price, url)
        
        return result


    def main(url) :
        # start up the webdriver
        driver = webdriver.Chrome(executable_path="/Users/jessica/Downloads/chromedriver")

        records = []
        for page in range (1,21):
            driver.get(url.format(page))
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = soup.find_all('div', {'data-component-type' : 's-search-result'})
            for item in results:
                record = extract_record(item)
                if(record):
                    records.append(record)
        driver.close()

        df = pd.DataFrame(records)
        df.rename(columns = {0 : "Description", 1 : "Price",  2 : "Url"}, inplace=True)
        df = df.sort_values(by='Price')
        d =  df.head(5).to_dict()
        d = json.dumps(d, sort_keys=True , indent=4)
        return d
    return main(url)
     

if __name__ == '__main__':
    app.run(debug=True)
