from flask import Flask, render_template
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)

