# ---------------------------- IMPORTS ------------------------------------- #
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

# ------------------------- APPLICATION ------------------------------------- #

# instantiate flask app
app = Flask(__name__)
api = Api(app)

#Instantiate products list and seed with starting data
products = {"clorox": {"name": "clorox", "ingredients": ["bleach", "water", "chlorine"]},
            "windex": {"name": "windex", "ingredients": ["water", "ammonia"]}}

# Base endpoint, lists all products
@app.get('/')
def list_all_products():
    return{"products":list(products.values())}

# list products and filter based on ingredient
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

# Add new product to the list
def create_product(new_product):
    product_name = new_product['name']
    products[product_name] = new_product
    return new_product

# Get and Post actions
@app.route('/products', methods=['GET', 'POST'])
def products_route():
    if request.method == 'GET':
        return list_products()
    elif request.method == "POST":
        return create_product(request.get_json(force=True))

# Return product by name
@app.route('/products/<product_name>')
def get(product_name):
    return products[product_name]

if __name__ == '__main__':
    app.run()
