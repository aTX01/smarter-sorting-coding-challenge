from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)
#api.add_resource(product, '/product')

products = {"Clorox": {"name": "clorox", "ingredients": ["sodium hypochlorite", "water", "sodium chloride"]},
            "Windex": {"name": "windex", "ingredients": ["water", "ammonium hydroxide"]}}

print("Dictionary:", products)

@app.get('/products')
def get_all():
    return {'products':list(products.values())}

# @app.route('/products/<product_name>')
# def get(product_name):
#     return products[product_name], 200

if __name__ == '__main__':
    app.run()
