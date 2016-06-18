#!/opt/isv/virtualenvs/lb_automation/bin/python

class box:
	def area(self):
		return self.width * self.height

	def __init__(self, width, height):
		self.width = width
		self.height = height

x = box(10, 2)
print(x.area())

#master test
#testing update
