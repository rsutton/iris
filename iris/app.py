from flask import Flask, request, jsonify, render_template
import numpy as np
import os
import pickle
from sklearn.svm import SVC

app = Flask(__name__)
REQUIRED_PARAMETERS = ('sepal_length', 'sepal_width', 'petal_length',
                       'petal_width')


@app.before_first_request
def load_model_to_app():
    this_dir = os.path.dirname(__file__)
    filename = os.path.join(this_dir, './static/model/model.pickle')
    with open(filename, 'rb') as fh:
        app.predictor = pickle.load(fh)


@app.route("/")
def index():
    return render_template('index.html', pred=0)


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    data = []
    results = {}
    # use request.form with POST, request.args would be for GETs
    for arg in request.form:
        if arg in REQUIRED_PARAMETERS:
            param = request.form.get(arg)
            data.append(param)
            results[arg] = param

    if len(data) < len(REQUIRED_PARAMETERS):
        return "<h1>Error - missing parameter</h1>"

    data = np.array([np.asarray(data, dtype=float)])
    prediction = app.predictor.predict(data)
    results['prediction'] = str(prediction[0])
    return jsonify(results)


def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == '__main__':
    main()