import json

people_string = '''{
    "people":[
    {
     "name":"Abhishek",
     "phone":"9663646078",
     "email":["abhisand100@gmail.com","abhishekchinnus@gmail.com"]

    },
    {
     "name":"Balu",
     "phone":"9663646078",
     "email":"balu@gmail.com"

    },
    {
     "name":"Abhilasha",
     "phone":"8884824553",
     "email":"abhilasha@gmail.com"

    }


]
}
'''

data = json.loads(people_string)
# print(data['people'])
for person in data['people']:
    # print(person['name'])
    del person['phone']

new_string = json.dumps(data,indent=3,sort_keys=True)
print(new_string)