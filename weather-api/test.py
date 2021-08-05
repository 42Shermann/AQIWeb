from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    req = requests.get('https://api.waqi.info/feed/'+zipcode+'/?token=562bec4318461b40df147d797a7dad8e87353035').json()
    data_req = req
    return render_template("temperature.html", aqi_data=data_req)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')    



if __name__ == '__main__':
    app.run(debug=True)