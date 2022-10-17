from distutils.util import execute
from colorama import Cursor
from flask import *
import mysql.connector
from datetime import datetime, timedelta

app=Flask(__name__)

app.secret_key='user' 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Akki@123",
  database="crs"
)


mycursor = mydb.cursor(buffered=True)

@app.route('/',methods=['POST','GET'])
def home0():
    print("ENTERED1")
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login0():
    print("ENTERED2")
    return render_template('login.html')

@app.route('/signin',methods=['POST','GET'])
def signin0():
    print("ENTERED3")
    return render_template('signin.html')   

@app.route('/forgetPassoword',methods=['POST','GET'])
def forgetpass0():
    print("ENTERED4")
    return render_template('forgetPass.html')       

app.run(debug=True)