from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/search/', methods=['GET'])
def get_data():
    search_req=request.args.get('q')
    return _webscrapping(search_req)

def _webscrapping(item):
    return "dummy results"

if __name__ == '__main__':
    app.run(debug=True)