import json
from urllib.request import urlopen

# with open('students.json') as f:
#     data = json.load(f)

# for student in data['people']:
#    del student['email']

# with open('newstudents.json','w') as f:
#     json.dump(data,f,indent=2)

with  urlopen("http://finance.yahoo.com/webservice/v1/symbols/COALINDIA.NS/quote?format=json&view=detail") as response:

    source = response.read()

print(source)
