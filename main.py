from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1+ num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return str(num1*num2)

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    return str(num1/num2)