# Dictionary in Python 
# Dictionaries are use to store data values in key:value pairs
# They are unordered, mutable(changeable), dont allow duplicate keys

# info = {
#     "name" : "Parth Patil",
#     "cgpa" : 9.5,
#     "marks" : [97, 98, 93],
#     "is_adult" : True,
# }
# print(info) #Output {'name': 'Parth Patil', 'cgpa': 9.5, 'marks': [97, 98, 93]}
# print(info["name"]) #Output Parth Patil
# info["name"] = "Rudresh Patil"
# info["name"] = "Daksh Patil"
# print(info["name"])
#-----------------------------------------------------------------------------------------------------------------------------------------

# Null Dictionary
# null = {}
# print(type(null))

#-----------------------------------------------------------------------------------------------------------------------------------------

# Nested Dictionary 
info = {
    "name": "Parth Patil",
    "marks": {
        "Chem": 93,
        "Phy": 93,
        "Maths": 93,
    },
    "Age": 18
}
print(info) #Output {'name': 'Parth Patil', 'marks': {'Chem': 93, 'Phy': 93, 'Maths': 93}, 'Age': 18}
print(info["name"]) #Output Parth Patil
print(info["marks"]["Chem"]) #Output 93
#-----------------------------------------------------------------------------------------------------------------------------------------

