class init_Demo:
	str = ""
	def __init__(self):
		print("Welcome to Default init() function")
	def __init__(self,msg):
		global  str
		self.str=msg
		print("Hi ",self.str)

obj=init_Demo(input("Enter the string Here..:"))