from flask import Flask, render_template, jsonify
from api_helper import get_restaurants_data

app = Flask(__name__)

@app.route('/')
def index():
    postcode = "BS14DJ" #swlected postcode
    restaurants_data = get_restaurants_data(postcode)
    return render_template('index.html', restaurants=restaurants_data)

if __name__ == "__main__":
    app.run(debug=True)
