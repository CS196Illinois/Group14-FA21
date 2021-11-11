import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd



def get_url(search_term):
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_2"
    search_term = search_term.replace(' ', "+")

    # add term to query url
    url = template.format(search_term)

    #add page query placeholder
    url += '&page{}'

    return url



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

    try:
        #rank and rating
        rating = item.i.text
        review_count = item.find('span', {'class': 'a-size-base', 'dir' : 'auto'}).text
    except AttributeError:
        rating = ""
        review_count = ""
    
    result = (description, price, rating, review_count, url)
    
    return result


def main(search_term) :
    # start up the webdriver
    driver = webdriver.Chrome(executable_path="/Users/jessica/Downloads/chromedriver")

    records = []
    url = get_url(search_term)

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
    df.rename(columns = {0 : "Description", 1 : "Price",  2 : "Rating", 3 : "ReviewCount", 4 : "Url"}, inplace=True)
    df = df.sort_values(by='Price')
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    d =  d = df.head(5).to_dict()
    return d

main('ultrawide monitor')

  
    

    





        
    

    


    
