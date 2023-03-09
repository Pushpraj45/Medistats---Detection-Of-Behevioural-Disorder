from flask import Flask, render_template, request
import numpy as np
import joblib
import pickle
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('prediction.sav', 'rb'))

# Define the home page
@app.route('/')
def home():
    return render_template('index1.html')

# Define the predict page
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    features = [x for x in request.form.values()]
    features = np.array(features).reshape(1, -1)  
    prediction = model.predict(features)
    if prediction == 1:
        output = 'high'
    else:
        output = 'low'
    return render_template('index1.html', prediction_text=f'The predicted chance of behavioural disorder is {output}.')

if __name__ == '__main__':
    app.run(debug=True)