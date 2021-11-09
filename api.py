from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

class product(Resource):
    def get(self):
        data = pd.read_csv('example_data.csv')
        data = data.to_dict()
        return {'data': data}, 200

app = Flask(__name__)
api = Api(app)
api.add_resource(product, '/product')


if __name__ == '__main__':
    app.run()
