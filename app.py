import joblib
import numpy as np
from flask import Flask,request,jsonify,render_template

app =Flask(__name__)

# Load the model
model = joblib.load('trained_model.joblib')

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = int(model.predict(features))
    # The map dictionary
    fish_mapping = {1: 'Bream', 2: 'Roach', 3: 'Whitefish', 4: 'Parkki', 5: 'Perch', 6: 'Smelt'}

    # Using the map to get the fish name
    predicted_fish = fish_mapping.get(prediction, 'Unknown')
    return render_template('index.html', prediction_text=f'The Fish species is {predicted_fish}')

if __name__=='__main__':
    app.run(debug=True)
