from flask import Flask, render_template
import json
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.yelp.com/v3'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'


@app.route('/')
def displayHomepage():
    """Return our home page to the user."""
    return render_template('index.html')


@app.route('/about')
def meetUs():
    """Return about page."""
    return render_template('about.html')


@app.route('/listings')
def listing():
    try:
        return render_template('listing.html')
    except (ValueError, TypeError):
        return render_template('500.html'), 500

def search(api_key, term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


if __name__ == '__main__':
    app.run(debug=True)

