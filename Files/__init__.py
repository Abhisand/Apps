import json
import os

if os.path.isfile("./database.json") and os.stat("./database.json").st_size != 0:
	old_file = open("./database.json","r+")
	data = json.loads(old_file.read())
	print("Hi ",data["name"],"Welcome to my tutorial")
	print("Currently ur doing an ",data["course"]," Course/s on udemy")

else:
	old_file = open("./database.json","w+")
	data = {"name": "Abhishek S", "course":"Java"}
	print("No database Found!\n ", data["name"], "And his courses are newly added into the database")

old_file.seek(0)
old_file.write(json.dumps(data))