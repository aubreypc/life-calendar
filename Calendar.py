from __future__ import division
from datetime import date, timedelta
from flask import render_template
from decimal import Decimal
import config

class Calendar(object):
	def __init__(self, startYear, startMonth, startDay, expectancy=config.DEFAULT_LIFE_EXPECTANCY):
		self.expectancy = expectancy
		self.birth_date = date(int(startYear), int(startMonth), int(startDay)) #todo: exception handling for invalid inputs
		self.expected_death_date = self.birth_date + timedelta(days=(365.25 * expectancy))
		self.today = date.today()

	def past_days(self):
		delta = self.today - self.birth_date
		if delta.days <= 0:
			raise Exception("Invalid age")	
		return delta.days

	def future_days(self):
		delta = self.expected_death_date - self.today
		if delta.days <= 0:
			raise Exception("Invalid age")
		return delta.days

	def render(self):
		weeks_spent = int(self.past_days() / 7)
		weeks_left = int(self.future_days() / 7)
		fraction = self.past_days() / (365.25 * self.expectancy)
		percentage = round(Decimal(fraction * 100), 2)
		return render_template('calendar.html', past=weeks_spent, future=weeks_left, percentage=percentage)
