import requests

my_data = {"name":"Abhishek s" ,"email":"Abhisand100@gmail.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php",my_data)
f = open("myfile.html","w+")
f.write(r.text)
print(r.text)