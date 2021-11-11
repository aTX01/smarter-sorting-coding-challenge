# Product List API #

This application demonstrates a REST API for interacting with a list of consumer products and ingredients. Users may create and retrieve product information.

## System Requirements ##

The application requires the following dependencies:
```
python (v3.6+)
flask
flask_restful
curl
```

On Ubuntu or Debian systems, these packages may be installed as follows:
```
$ sudo apt install python3
$ sudo apt install python3-flask
$ sudo apt install python3-flask-restful
$ sudo apt install curl
```

Alternatively, the python packages may be installed with pip as follows:
```
$ sudo pip install flask
$ sudo pip install flask-restful
```

## Running Application ##

Within a terminal, start the application as follows:
```
$ export FLASK_APP=product_list_api.py
$ flask run
```

By default, flask will serve the application at http://127.0.0.1:5000/


### Using Application ###

Interacting with the API may be done using `curl`.

Run the application in one terminal as described in the previous section. In a second terminal, run curl commands. Common commands are as follows:

To `POST` new products to the list:
```
curl -X POST http://127.0.0.1:5000/products
      -H 'Content-Type: application/json'
      -d '{"name": "<product_name>", "ingredients":["<ingredient1>", "<ingredient2>", ...]}'
```

*NOTE*: The application product list is pre-populated with some example products.

To `GET` full products list:
```
$ curl -X GET http://127.0.0.1:5000/

#or

$ curl -X GET http://127.0.0.1:5000/products

```

To `GET` products containing a certain ingredient:
```
$ curl -X GET -G http://127.0.0.1:5000/products -d "ingredient=<ingredient_name>"
```
For example:
```
$ curl -X GET -G http://127.0.0.1:5000/products -d "ingredient=water"
```

To `GET` a particular product entry:
```
$ curl -X GET http://127.0.0.1:5000/products/<product_name>
```
For example:
```
$ curl -X GET -G http://127.0.0.1:5000/products/clorox
```

### Endpoints ###

The application includes the following endpoints
http://127.0.0.1:5000/: provides a list of all products currently in the list

http://127.0.0.1:5000/products: GET or POST to the products list at this endpoint. The returned product list may be filtered by ingredients, or is returned in full by default.

http://127.0.0.1:5000/products/<product_name>: Return information on specific product
