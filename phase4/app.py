from flask import Flask, request, render_template
app = Flask(__name__)

global var
var = 0

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/val')
def get_val():
    global var
    return {'val': var}

@app.route('/update')
def update():
    global var
    var += 1
    return {'res': 'updated'}
