from flask import Flask, jsonify, request
from flask_restx import Resource, Api, reqparse
import requests

app = Flask(__name__)
api = Api(app)
app.config['DEBUG'] = True


@app.route('/dd')
def index():
    return 'Hello juntheworld'


@api.route('/traces')  # url pattern으로 name 설정
class testAPI(Resource):
    def get(self):
        xStart = request.args.get('xStart', 1.0)
        yStart = request.args.get('yStart', 1.0)
        xEnd = request.args.get('xEnd', 1.0)
        yEnd = request.args.get('yEnd', 1.0)
        return {
            "xStart": xStart,
            "yStart": yStart,
            "xEnd": xEnd,
            "yEnd": yEnd,
        }

    # def post(self):
    #     iris = load_iris()
    #     parsed_request = request.json.get('content')
    #     result = iris.feature_names

    #     print(parsed_request)
    #     return result


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
