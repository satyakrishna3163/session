#How would you read and write JSON files in Python

import json
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)
print(json_object)  