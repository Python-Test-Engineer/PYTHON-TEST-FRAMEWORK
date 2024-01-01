import json

from utilities.boxen import bx_info, bx_result

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'

# Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(dict_courses)
print(dict_courses["name"])
# get me the first language taught by trainer
list_language = dict_courses["languages"]
print(type(list_language))
print(list_language[0])
print(dict_courses["languages"][0])

print("+++++++++++++++++++++++++++++++++")

with open("./data/courses.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))
    bx_result(f"{data["courses"]["name"]} is {data['courses']['age']} years old")
 
