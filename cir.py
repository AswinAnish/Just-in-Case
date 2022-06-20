import math as m
class circle():
	r=0.0
	def val(self):
		self.r = float(input("Enter the Radius "))
	def area(self):
		area = m.pi*(self.r*self.r)
		print(area)
	def peri(self):
		peri = 2*m.pi*self.r
		print(peri)
r=circle()
r.val()
r.area()
r.peri()
	





