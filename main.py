
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

class CalculatorForm(FlaskForm):
    num1 = IntegerField('First Number', validators=[DataRequired()])
    num2 = IntegerField('Second Number', validators=[DataRequired()])
    operation = SelectField('Operation', choices=[('add', 'Add'),('subtract','Subtract'),('multiply', 'Multiply'), ('divide', 'Divide')])
    submit = SubmitField('Calculate')

@app.route('/', methods=['GET', 'POST'])
def CalcForm():
    form = CalculatorForm()
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        operation = form.operation.data
        return redirect(url_for(operation, num1=num1, num2=num2))
    return render_template('form.html', form=form)



@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Addition Result</title>
    </head>
    <body>
        <h1>Result: {result}</h1>
        <button onclick="window.history.back();">Go Back</button>
    </body>
    </html>
    '''
    return html

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    result = num1 - num2
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Addition Result</title>
    </head>
    <body>
        <h1>Result: {result}</h1>
        <button onclick="window.history.back();">Go Back</button>
    </body>
    </html>
    '''
    return html

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Multiplication Result</title>
    </head>
    <body>
        <h1>Result: {result}</h1>
        <button onclick="window.history.back();">Go Back</button>
    </body>
    </html>
    '''
    return html

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    result = num1 / num2
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Division Result</title>
    </head>
    <body>
        <h1>Result: {result}</h1>
        <button onclick="window.history.back();">Go Back</button>
    </body>
    </html>
    '''
    return html