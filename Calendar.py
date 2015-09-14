import config
from datetime import date, timedelta
from flask import render_template

class Calendar(object):
	def __init__(self, startYear, startMonth, startDay, expectancy=config.DEFAULT_LIFE_EXPECTANCY):
		self.birth_date = date(int(startYear), int(startMonth), int(startDay)) #todo: exception handling for invalid inputs
		self.expected_death_date = self.birth_date + timedelta(days=(365.25 * expectancy))
		self.today = date.today()

	def past_days(self):
		delta = self.today - self.birth_date
		return delta.days

	def future_days(self):
		delta = self.expected_death_date - self.today
		return delta.days

	def render(self):
		weeks_spent = int(self.past_days() / 7)
		weeks_left = int(self.future_days() / 7)
		return render_template('calendar.html', past=range(weeks_spent), future=range(weeks_left))