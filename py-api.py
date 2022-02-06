import flask
from flask import request
import json, time
import requests, json

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    name_surname = {'name': 'B.Emre', 'surname': 'Ozturk'}
    home_page = json.dumps(name_surname)
    return home_page

@app.route('/temperature', methods=['GET'])
def temp_page():
    city = request.args.get("city")
    URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=0c1c53d27c1f881f8eb4c80f1611d2b9&units=metric".format(city)
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        print(f"Temperature: {temperature}")

    else:
        print("Error in the HTTP request")

    city_temp = {'temperature': temperature}
    temp_page = json.dumps(city_temp)
    return temp_page

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')