class Circle:
	pi = 3.14
	def __init__(self,radius):
		self.radius =radius

	def areaofcircle(self):
		a = Circle.pi * (self.radius)**2
		return a

o1 = Circle(5)

print(o1.areaofcircle())