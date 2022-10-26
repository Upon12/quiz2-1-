import json
import os
import re
import shutil
import csv
import sys
import pyodbc
from io import BytesIO
# from turtle import title, width
from flask import Flask,render_template, url_for, flash, redirect, request
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
# from wtforms import StringField, IntegerField, SubmitField, SelectField
# from wtforms.validators import DataRequired
from PIL import Image

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'pxh2153'

# ROUTES!
@app.route('/',methods=['GET','POST'])
def question10a():
	if request.method=='GET':
		return render_template('question10a.html',question10a_active = "active",title="question 10a")
	if request.method=='POST':
		low=int(request.form["Low"])
		high=int(request.form["High"])
		if(low>high):
			a=low
			low=high
			high=a
		if low>0 and high>0:
			cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:hpspdb.database.windows.net,1433;Database=sampdb;Uid=hp;Pwd={Cf123456};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
			cursor = cnxn.cursor()
			cursor.execute("select sum(num),food from f where store>=? and store<=? group by food",low,high)
			a = cursor.fetchall()
			count=[]
			name=[]
			for item in a:
				count.append(item[0])
				name.append(item[1])
			dic={}
			dic['count']=count
			dic['name']=name
			dataJson=json.dumps(dic,ensure_ascii=False)
			return render_template('question10a.html',question10a_active = "active",data = dataJson,title="question 10a")
		else:
			return render_template('question10a.html',question10a_active = "active",information="Your input is wrong!",title="question 10a")



@app.route('/question10b',methods=['GET','POST'])
def question10b():
	if request.method=='GET':
		return render_template('question10b.html',question10b_active = "active",title="question 10b")
	if request.method=='POST':
		low=int(request.form["Low"])
		high=int(request.form["High"])
		if(low>high):
			a=low
			low=high
			high=a
		if low>0 and high>0:
			cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:hpspdb.database.windows.net,1433;Database=sampdb;Uid=hp;Pwd={Cf123456};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
			cursor = cnxn.cursor()
			cursor.execute("select sum(num),store from f where store>=? and store<=? group by store ",low,high)
			a = cursor.fetchall()
			count=[]
			name=[]
			for item in a:
				count.append(item[0])
				name.append(item[1])
			dic={}
			dic['count']=count
			dic['name']=name
			dataJson=json.dumps(dic,ensure_ascii=False)
			return render_template('question10b.html',question10b_active = "active",data = dataJson,title="question 10b")
		else:
			return render_template('question10b.html',question10b_active = "active",information="Your input is wrong!",title="question 10b")

@app.route('/question12',methods=['GET','POST'])
def question12():
	if request.method=='GET':
		return render_template('question12.html',question12_active = "active",title="question 12")
	if request.method=='POST':
		low=int(request.form["Low"])
		high=int(request.form["High"])
		if(low>high):
			a=low
			low=high
			high=a
		if low>0 and high>0:
			cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:hpspdb.database.windows.net,1433;Database=sampdb;Uid=hp;Pwd={Cf123456};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
			cursor = cnxn.cursor()
			cursor.execute("select sum(num),store from f where store>=? and store<=? group by store ",low,high)
			a = cursor.fetchall()
			count=[]
			name=[]
			for item in a:
				count.append(item[0])
				name.append(item[1])
			dic={}
			dic['count']=count
			dic['name']=name
			dataJson=json.dumps(dic,ensure_ascii=False)
			return render_template('question12.html',question12_active = "active",data = dataJson,title="question 12")
		else:
			return render_template('question12.html',question12_active = "active",information="Your input is wrong!",title="question 12")

@app.route('/question11a',methods=['GET','POST'])
def question11a():
	if request.method=='GET':
		cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:hpspdb.database.windows.net,1433;Database=sampdb;Uid=hp;Pwd={Cf123456};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
		cursor = cnxn.cursor()
		cursor.execute("select x,y,color from p where color='r'")
		a = cursor.fetchall()
		count=[]
		color=[]
		for item in a:
			count.append(list(item[0:2]))
			color.append(item[2])
		dic={}
		dic['count']=count
		dic['color']=color
		dataJson=json.dumps(dic,ensure_ascii=False)
		cursor.execute("select x,y,color from p where color='g'")
		a1 = cursor.fetchall()
		count1=[]
		color1=[]
		for item in a1:
			count1.append(list(item[0:2]))
			color1.append(item[2])
		dic1={}
		dic1['count']=count1
		dic1['color']=color1
		dataJson1=json.dumps(dic1,ensure_ascii=False)
		return render_template('question11a.html',question11a_active = "active",data = dataJson,data1 = dataJson1,title="question 11a")

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')


# if __name__ == '__main__':
# 	app.run()

port = int(os.getenv('PORT','3000'))
app.run(debug=True,host='0.0.0.0',port=port)