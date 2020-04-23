import datetime
import pytz
import cgi, cgitb
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/info',methods=["POST"])
def info():
    name = request.form['name']
    location = request.form['location']
    return render_template( 'test2.html',name=name,location=location)

@app.route('/')
def test():
    return render_template('index.html')


@app.route('/tes2')
def tes2():
    return render_template('tes2.html')


if __name__ == '__main__':
    app.run(debug=True)