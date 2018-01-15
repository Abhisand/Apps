class Demo:
	x = 10
	y = 10
	def show(self,a,b):
		global x,y
		self.x = a
		self.y = b
		print("The value of x -> ",self.x)
		print("The value of y -> ",self.y)


obj=Demo()
obj.show(input("Enter the Value of X:"),input("Enter the value of Y:"))