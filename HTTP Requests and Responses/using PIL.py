import requests
from  io import  BytesIO
from PIL import Image

r = requests.get("http://www.freepngimg.com/thumb/jobs/12-2-jobs-png-hd-thumb.png")
print(r.status_code)

myimage = Image.open(BytesIO(r.content))
print(myimage.size,myimage.format,myimage.mode)
mypath = "./image."+myimage.format
try:
	myimage.save(mypath,myimage.format)
except IOError:
	print("Cannot Save the image")