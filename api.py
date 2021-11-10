from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)
#api.add_resource(product, '/product')

products = {"clorox": {"name": "clorox", "ingredients": ["sodium", "water", "chlorine"]},
            "windex": {"name": "windex", "ingredients": ["water", "ammonium"]}}

print("Dictionary:", products)

@app.get('/all_products')
def list_all_products():
    return{"products":list(products.values())}

@app.get('/products')
def list_products():
    ingredient = request.args.get('ingredient')
    if ingredient:
        qualifying_data = list(
            filter(
                lambda p1: str(ingredient) in p1['ingredients'],
                products.values()
            )
        )
        return {'products':qualifying_data}
    else:
        return{"products":list(products.values())}

@app.route('/products/<product_name>')
def get(product_name):
    return products[product_name]

if __name__ == '__main__':
    app.run()
