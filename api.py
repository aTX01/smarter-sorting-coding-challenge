from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_database():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE']
            detect_types=sqlite3.PARSE_DECLITYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

class product(Resource):
    def __init__(self):
        self.products = pd.read_csv('example_data.csv').to_dict()

    def get(self, product):
        return self.products[product], 200

    def get_all(self):
        return {'products': self.products}, 200


app = Flask(__name__)
api = Api(app)
#api.add_resource(product, '/product')

products = pd.read_csv('example_data.csv').to_dict()

print("Dictionary:", products)

@app.get('/products')
def get_all():
    return {'products': products}, 200

@app.route('/products/<product_name>')
def get(product_name):
    return products[product_name], 200

if __name__ == '__main__':
    app.run()
