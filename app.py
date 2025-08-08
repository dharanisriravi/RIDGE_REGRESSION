
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open('model/ridge_model.pkl', 'rb') as f:
    model = pickle.load(f)

# LabelEncoder mapping
season_map = {"summer": 2, "winter": 1, "monsoon": 0}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hour = int(request.form['hour'])
    temperature = float(request.form['temperature'])
    appliance_usage = int(request.form['appliance_usage'])
    season = season_map[request.form['season'].lower()]
    humidity = float(request.form['humidity'])

    features = np.array([[hour, temperature, appliance_usage, season, humidity]])
    prediction = model.predict(features)[0]

    return render_template('result.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
