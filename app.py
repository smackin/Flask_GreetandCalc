from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add(): 
    a = request.args.get('a')
    b = request.args.get('b')
    result =  add(a, b)
    
    return str(result)

@app.route('/sub')
def subtract():
    a = request.args.get('a')
    b = request.args.get('b')
    result =  sub(a, b)
    
    return str(result)

@app.route('/multiply')
def multiply():
    a = request.args.get('a')
    b = request.args.get('b')
    result =  mult(a, b)
    
    return str(result)

@app.route('/divide')
def divide():
    a = request.args.get('a')
    b = request.args.get('b')
    result =  div(a, b)
    
    return str(result)