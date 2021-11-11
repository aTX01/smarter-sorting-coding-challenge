from flask import Flask, request, g
from flask_restful import Resource, Api, reqparse
import sqlite3


app = Flask(__name__)
api = Api(app)
#api.add_resource(product, '/product')

products = {"clorox": {"name": "clorox", "ingredients": ["sodium", "water", "chlorine"]},
            "windex": {"name": "windex", "ingredients": ["water", "ammonium"]}}

print("Dictionary:", products)

connection = sqlite3.connect('products.db')
cursor = connection.cursor()
command1 = """CREATE TABLE IF NOT EXISTS
products(name TEXT PRIMARY KEY, ingredients TEXT)"""
cursor.execute(command1)
DATABASE='./products.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    def convert_to_dicts(cursor, row):
        return dict((cursor.description[i][0], val)
            for i, val in enumerate(row))

    db.row_factory = convert_to_dicts

    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    print("rv", rv)
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.get('/all_products')
def list_all_products():
    cur = get_db().cursor()
    database = get_db()
    print(query_db('SELECT * FROM products'))
    #return query_db('select * from products')
    # return{"products":list(products.values())}

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

def create_product(new_product):
    product_name = new_product['name']
    products[product_name] = new_product
    return new_product

@app.route('/products', methods=['GET', 'POST'])
def products_route():
    if request.method == 'GET':
        return list_products()
    elif request.method == "POST":
        return create_product(request.get_json(force=True))


@app.route('/products/<product_name>')
def get(product_name):
    return products[product_name]

if __name__ == '__main__':
    app.run()
