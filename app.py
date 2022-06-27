import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
# Define API KEY, ENDPOINTS, AND HEADERS HERE
API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.yelp.com/v3'
BUSINESS_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}


# Define our parameters and what we want a response to be
PARAMETERS = {
    'categories': 'food',
    'limit': 20,
    'radius': 10000,
    'price': 1,
    'is_close': False,
    'location': 'Oakland'
}
# Make a request to the API
response = requests.get(url=BUSINESS_ENDPOINT,
                        params=PARAMETERS, headers=HEADERS)

category_data = response.json()

@ app.route('/')
def display_categories():
    business_array = []
    for biz in category_data['businesses']:
        business_array.append(biz)
    return render_template('index.html', context=business_array)


@ app.route('/about')
def meetUs():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
