# How would you use Python to write a dictionary to a JSON file

import json
dictionary ={
    "name" : "satyakrishna",
    "rollno" : 49,
    "cgpa" : 6.8,
    "phonenumber" : "8500803155"
}
    

d = json.dumps(dictionary)
print(d)