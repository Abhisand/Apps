import json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
	old_file = open("./ages.json","r+")
	data = json.loads(old_file.read())
	print("The Current age is ",data["age"],"__adding a Year")
	data["age"] = data["age"] + 1
	print("New Age is :",data["age"])
else:
	old_file = open("./ages.json","w+")
	data = {"name":"Abhishek","age":20}
	print("No File found hence setting age to ",data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))