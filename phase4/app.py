import obd, time
from model import values as vals
from model import connection as conn
from flask import Flask, request, render_template


app = Flask(__name__)

global connection
global values_

def initialize():
    global values_
    global connection
    values_ = vals.values()
    connection = conn.connection(values_)

initialize()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/val')
def get_val():
    global values_
    return {'val': values_.get_test()}

@app.route('/update')
def update():
    global connection
    connection.update_test()
    return {'res': 'updated'}
