import  requests

myparam = {"q":"pizza"}
r = requests.get("https://www.bing.com/search?",params=myparam)

print(r.status_code)
f = open("dummy.html","w+")
print(r.url)
f.write(r.text)