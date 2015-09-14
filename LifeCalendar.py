from flask import Flask, render_template
from Calendar import Calendar

app = Flask("LifeCalender")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/calendar/<year>/<month>/<day>")
def showCalendar(year, month, day):
	cal = Calendar(year, month, day)
	return cal.render()
