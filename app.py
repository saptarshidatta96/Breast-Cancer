from flask import Flask, request, jsonify
import joblib
import pandas as pd



app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])


def predict():
    if knn_model:
        try:
            if request.get_json() is not None:
                json_ = request.json
                query = pd.get_dummies(pd.DataFrame(json_))
                query = query.reindex(columns=model_columns, fill_value=0)
                prediction = list(knn_model.predict(query))

                return jsonify({'prediction': str(prediction),
                                'Input': request.json})
            else:
                
                json_ = [request.args]
                query = pd.get_dummies(pd.DataFrame(json_))
                query = query.reindex(columns=model_columns, fill_value=0)
                prediction = list(knn_model.predict(query))

                return jsonify({'prediction': str(prediction),
                                'Input': [request.args]})

        except Exception as e:

            return jsonify({'error': e})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':

    knn_model = joblib.load("breast_cancer_knn_model.pkl")
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl")
    print ('Model columns loaded')
    app.run(host='0.0.0.0', port=12345, debug=True)