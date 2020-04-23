import datetime
import pytz
import cgi, cgitb
from flask import Flask, request, render_template

app = Flask(__name__)


def time(wtime):
    if (wtime == 'UTC'):
        worldtime = datetime.datetime.now(pytz.timezone('UTC'))
    elif (wtime == 'Poland'):
        worldtime = datetime.datetime.now(pytz.timezone('Poland'))  # France, Poland, Germany, Italy, Austria +1
    elif (wtime == 'Turkey'):
        worldtime = datetime.datetime.now(pytz.timezone('Turkey'))  # 터키 +2
    elif (wtime == 'US/Eastern'):
        worldtime = datetime.datetime.now(pytz.timezone('US/Eastern'))  # 미국 동부 -5
    elif (wtime == 'Singapore'):
        worldtime = datetime.datetime.now(
            pytz.timezone('Singapore'))  # China, Indonesia(Central), Malaysia, Singapore +8
    elif (wtime == 'Asia/Seoul'):
        worldtime = datetime.datetime.now(pytz.timezone('Asia/Seoul'))  # 서울
    now1 = str(worldtime)
    now2 =now1[0:19]
    return now2

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/world', methods=['POST'])
def world():
    worldtime = request.form['Time']   
    now = time(worldtime)
    # return now
    return now

