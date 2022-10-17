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

@app.route('/index',methods=['POST','GET'])
def home0():
    print("ENTERED")
    return render_template('index.html')



