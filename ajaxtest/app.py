from datetime import datetime
import pytz
import cgi, cgitb
import json
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request2', methods =['POST'])
def request2():
    value = request.form['SensorID']
    print(value)
    # dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
    # jsondata=json.dumps(dic)    
    # hi ="dd"
    now = datetime.now() 
    worldtime = str(now)
    return worldtime

