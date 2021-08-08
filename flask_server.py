from flask import Flask, jsonify, request
from flask_restx import Resource, Api, reqparse
import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import requests

app = Flask(__name__)
api = Api(app)
app.config['DEBUG'] = True

@app.route('/dd')
def index():
    return 'Hello juntheworld'

@api.route('/test')
class testAPI(Resource):
    def get(self):
        return jsonify({"resut":"hihi juntheworld"})
    
    def post(self):
        iris = load_iris()
        parsed_request = request.json.get('content')
        result = iris.feature_names

        print(parsed_request)
        return result

if __name__ == "__main__":
    app.run(debug=True)

# URL = 'https://apis.openapi.sk.com/tmap/routes?'
# data = {'version'  : '1',
# "appKey" : "a872035b-eb08-4280-98e7-0dfd8388c5db",
# "startX" : "126.930128",
# "startY" : "37.6038190",
# "endX" : "126.928861",
# "endY" : "37.6026560"}

# response = requests.post(URL, data = data)
# response.encoding = 'utf-8'

# print(response.text)

