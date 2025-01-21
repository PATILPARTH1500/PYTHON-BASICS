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
# print(info.get("name2")) #Output None this method does not gives error only show none while print(info["name2"]) will give error

# #Update Method
# info.update({"city" : "Turbhe"})
# print(info) #Ouput  {'name': 'Parth Patil', 'marks': {'Chem': 93, 'Phy': 93, 'Maths': 93}, 'Age': 18, 'city': 'Turbhe'}
#You can also add another dictionary but if the keys are similar in both the dictionary the values may replaced.
#--------------------------------------------------------------------------------------------------------------------------------------------

#Sets in Python
#Set is the collection of the unordered items
#Each elements in the set must be unique & immutable also this statement says that elements of the set is immutable not the set 
#Set is mutable
#List and Dictionary cannot be in the sets beacuse they are muttable
#List and Dictionary are unhashable because there hash values can be changed 

# collection = {1, 2, 3, 4, 2, 3, "Hello" , "World" , "Hello"}
# print(collection) #Output {1, 2, 3, 4, 'Hello', 'World'} It will always ignore the duplicate elements in the set
# print(len(collection)) #Output 6 Length function will also ignore the duplicate elements of the sets
# print(type(collection)) #Output <class 'set'>
#--------------------------------------------------------------------------------------------------------------------------------------------

# Empty Set
# null = set() # This is an empty set
#--------------------------------------------------------------------------------------------------------------------------------------------

#Sets Method

#Add Method
# collection = set()
# collection.add(12)
# collection.add("parth")
# collection.add((1, 2, 3, 4))
# print(collection) #Output {(1, 2, 3, 4), 12, 'parth'}
# print(len(collection)) #It only counts the element type not the actual element #Output 3
#--------------------------------------------------------------------------------------------------------------------------------------------

# #Remove Method 
# collection.remove(12)
# print(collection) #Output {(1, 2, 3, 4), 'parth'}
#--------------------------------------------------------------------------------------------------------------------------------------------

#Clear Method
# collection.clear()
# print(collection) #Output set() it gives an empty set
#--------------------------------------------------------------------------------------------------------------------------------------------

#Pop Method
#collection.pop() Randomly picks any value from the above set
#--------------------------------------------------------------------------------------------------------------------------------------------

# #Union Method
# collection1 = {1, 2, 3, 4, 5}
# collection2 = {5, 4, 3, 2, 1}
# collection1.union(collection2)
# print(collection1) #Output {1, 2, 3, 4, 5}
#--------------------------------------------------------------------------------------------------------------------------------------------

# #Intersection Method
# collection1 = {1, 2, 3, 4, 5}
# collection2 = {6, 7, 4, 3, 2,}
# collection1.intersection(collection2)
# print(collection1)
#--------------------------------------------------------------------------------------------------------------------------------------------

# Quiz

# Write a python program to store following word meanings in the python dictionary
#table : "a piece of furniture" , "list of facts & figures"
#cat : "a small animal"

# quiz = {
#     "table"  : "a piece of furniture", "List of facts & figures"
#     "cat" : "a small animal"
# }
# print(quiz)
#--------------------------------------------------------------------------------------------------------------------------------------------


#Write a python program you are given a list for students. Assume one classroom is requried for 1 subjects How many classrooms are needed 
# all students

# subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C" }
# print(len(subjects))
# ans is 5
#--------------------------------------------------------------------------------------------------------------------------------------------

#Write a python program to enter the marks of 3 subjects from the user and store them in a dictionary . Start with an empty dictonary and
#add one by one . use subject as name as key and marks as values

# sub = {}

# x = int(input("enter the marks of the maths: "))
# sub.update({"Maths" : x})

# y = int(input("enter the marks of the chemistry: "))
# sub.update({"Chem": y})

# z = int(input("enter the marks of the maths: "))
# sub.update({"Phy" : z})

# print(sub)
#--------------------------------------------------------------------------------------------------------------------------------------------

