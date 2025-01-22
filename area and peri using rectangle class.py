class rect:
	def__init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
	def perimeter(self):
		return 2*(self.length+self.breadth)
		

a=int(input("enter the length:"))
b=int(input("enter the breadth:"))
obj=rect(a,b)
print("area of rectangle is",obj.area())
print("perimeter of rectangle is",obj.perimeter())
