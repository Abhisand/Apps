import requests
import json

headers = {"Content-Type": "application/json"}
url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl":"http://example.com"}
r = requests.post(url,json=payload,headers=headers)
print(r.text)