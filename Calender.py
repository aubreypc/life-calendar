import config

class Calender(Object):
	def __init__(self, startYear, startMonth, startDay, expectancy=config.DEFAULT_LIFE_EXPECTANCY):
		self.year = startYear
		self.month = startMonth
		self.day = startDay
		self.expectancy = expectancy

	def render(self):
		pass
