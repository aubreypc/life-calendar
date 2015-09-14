import config
from datetime import datetime

class Calendar(object):
	def __init__(self, startYear, startMonth, startDay, expectancy=config.DEFAULT_LIFE_EXPECTANCY):
		self.expectancy = expectancy
		dt = datetime(startYear, startMonth, startDay)

	def render(self):
		pass
