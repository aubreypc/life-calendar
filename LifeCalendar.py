from flask import Flask
from Calendar import Calendar

app = Flask("LifeCalender")

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/calender/<year>/<month>/<day>")
def showCalendar(year, month, day):
	cal = Calendar(year, month, day)
	return cal.render()
