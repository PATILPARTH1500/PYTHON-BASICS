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

# # Nested Dictionary 
# info = {
#     "name": "Parth Patil",
#     "marks": {
#         "Chem": 93,
#         "Phy": 93,
#         "Maths": 93,
#     },
#     "Age": 18
# }
# print(info) #Output {'name': 'Parth Patil', 'marks': {'Chem': 93, 'Phy': 93, 'Maths': 93}, 'Age': 18}
# print(info["name"]) #Output Parth Patil
# print(info["marks"]["Chem"]) #Output 93
# print(info.keys()) #Output dict_keys(['name', 'marks', 'Age'])
#-----------------------------------------------------------------------------------------------------------------------------------------

# Dictionary Methods


# info = {
#     "name": "Parth Patil",
#     "marks": {
#         "Chem": 93,
#         "Phy": 93,
#         "Maths": 93,
#     },
#     "Age": 18
# }

# #Keys Method
# print(info.keys()) #Output dict_keys(['name', 'marks', 'Age'])
# print(len(list(info.keys()))) #Output 3

# #Values Method
# print(info.values()) #Output dict_values(['Parth Patil', {'Chem': 93, 'Phy': 93, 'Maths': 93}, 18])
# print(len(info.values())) #Output 3

# #Items Method
# print(info.items()) #Output dict_items([('name', 'Parth Patil'), ('marks', {'Chem': 93, 'Phy': 93, 'Maths': 93}), ('Age', 18)])
# #It contains list having tuples inside in it. And the Tuples contains the key value pair of the dictionary
# print(len(info.items())) #Output 3

# #Get Method
# print(info.get("name")) #Output Parth Patil
# print(info.get("name2")) #Output None this method does not gives error only show none while print(info["name"]) will give error

# #Update Method
# info.update({"city" : "Turbhe"})
# print(info) #Ouput  {'name': 'Parth Patil', 'marks': {'Chem': 93, 'Phy': 93, 'Maths': 93}, 'Age': 18, 'city': 'Turbhe'}
#You can also add another dictionary but if the keys are similar in both the dictionary the values may replaced.
#--------------------------------------------------------------------------------------------------------------------------------------------

#Sets in Python
#Set is the collection of the unordered items
#Each elements in the set must be unique & immutable