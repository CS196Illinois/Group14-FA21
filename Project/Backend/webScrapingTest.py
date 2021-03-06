import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd


amazon_url = "https://www.amazon.com/s?k=ultrawide+monitor&ref=nb_sb_noss_2"
target_url = "https://www.target.com/s?searchTerm=bar+soap"
walgreens_url = "https://www.walgreens.com/search/results.jsp?Ntt=pencil"
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15'}
sauce =  urllib.request.urlopen(walgreens_url).read()
soup = BeautifulSoup(sauce, 'html.parser')


def extract_price(item):
    # Extract and records data of a single item

    try :
        # price
        price_parent = item.find('span' , 'product__price font__sixteen color__text-red')
        price = price_parent.find('span', 'sr-only').text
    except AttributeError:
        try :
            # price
            price_parent = item.find('span' , 'product__price font__sixteen wag-inline-txt')
            price = price_parent.find('span', 'sr-only').text
        except AttributeError:
            return
    return price

def extract_title(item):
    # Extract and records title of a single item
    try :
        # price
        title_parent = item.find('div', class_= 'product__title font__fourteen')
        title = title_parent.find('strong', class_='description').text.strip()
    except AttributeError:
        return
    return title


# Array of prices as floats
records = []
results = soup.find_all('div',{'class': 'item card card__product'})

for item in results:
    record = extract_price(item)
    if(record):
        records.append(record)

records_float = []
for item in records:
    records_float.append(float(item[1:]))

# Array of all titles 
titles = []
for item in results:
    title = extract_title(item)
    if(title):
        titles.append(title)

def cheapest_five(prices, titles):
    # Return cheapest five prices from list of prices passed in as parameter
    df = pd.DataFrame(titles)
    df["price"] = prices
    df.rename(columns = {0 : "name", "price" : "price"}, inplace=True)
    df = df.sort_values(by='price')
    return df.head(5)

print(cheapest_five(records_float,titles))

