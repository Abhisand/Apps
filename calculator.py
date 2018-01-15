import  re
print("Magical Calculator!")
print("Type 'quit' to Exit")
previous = 0
run = True

def show():
   global  run,previous
   if previous == 0:
      equation=input("Enter Equation:")
   else:
      equation=input(str(previous))
   if equation == "quit":
      run = False
   else:
      equation=re.sub('[aA-zZ,<>"£$(),/?.,@"]',"",equation)
      if previous == 0:
         previous=eval(equation)
      else:
         previous=eval(str(previous) + equation)


while run:
   show()

