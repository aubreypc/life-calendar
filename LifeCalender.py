from flask import Flask
from calender import Calender

app = Flask("LifeCalender")

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/calender/<year>/<month>/<day>")
def showCalender(year, month, day):
	cal = Calender(year, month, day)
	return cal.render()
