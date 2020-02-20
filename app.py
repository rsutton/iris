from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.svm import SVC

app = Flask(__name__)

@app.before_first_request
def load_model_to_app():
    app.predictor = pickle.load(open('./static/model/model.pickle', 'rb'))
    

@app.route("/")
def index():
    return render_template('index.html', pred = 0)

@app.route('/predict', methods=['POST'])
def predict():
    data = [request.form['spatial_length'],
            request.form['spatial_width'],
            request.form['petal_length'], 
            request.form['petal_width']]
    data = np.array([np.asarray(data, dtype=float)])

    prediction = app.predictor.predict(data)
    print('INFO Prediction: {}'.format(prediction[0]))

    return render_template('index.html', pred=prediction[0])

def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000, debug=False)  # nosec


if __name__ == '__main__':
    main()