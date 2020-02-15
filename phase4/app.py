import obd
from flask import Flask, request, render_template
app = Flask(__name__)

global var
global connection
global rpm
rpm = 0
var = 0

def initialize():

    global connection
    connection = obd.Async(portstr="/dev/rfcomm0", fast=False)

    connection.watch(obd.commands.RPM, callback=update_rpm)
    connection.start()

def update_rpm(rev):
    global rpm
    rpm = rev.value.magnitude

initialize()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/rpm')
def get_rpm():
    global rpm
    return {'rpm': rpm}

@app.route('/val')
def get_val():
    global var
    return {'val': var}

@app.route('/update')
def update():
    global var
    var += 1
    return {'res': 'updated'}

@app.route('/end')
def end():
    global connection
    connection.stop()
    return "connection stopped"
