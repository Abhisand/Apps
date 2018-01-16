import requests

r = requests.get("http://www.google.com")
print("Status",r.status_code)
print(r.url)
f = open("page.html","w+")
f.write(r.text)