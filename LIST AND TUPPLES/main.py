#LIST IN PYHTON

# Marks = [12, 12, 12, 2]
# print(Marks)
# print(type(Marks))
# print(Marks[0])
# print(Marks[0:3])
#-----------------------------------------------------------------------------------------------------------------------------------------

# str = ["Parth", 95 , "Cet"]
# print(str)
# print(type(str))
# print(str[0])
#-----------------------------------------------------------------------------------------------------------------------------------------

# List are muttable 
# str = ["Parth", "Rudra", "Reet", "Daksh", "Vikrant" ]
# str[4] = "Akshat"
# print(str)
#-----------------------------------------------------------------------------------------------------------------------------------------

#List Methods
# list = [1, 2, 3, 4, 5 ]

#Append methods it just add the element to the end of the list
# list.append(6) #Output [1, 2, 3, 4, 5, 6]
# print(list)

# #Sort methods it just sort the element in numeric wise & aplhabetical order
# list.sort()
# print(list) #Output [1, 2, 3, 4, 5, 6]

# Sorting Methods
# list.sort(reverse=True)
# print(list) #Output [6, 5, 4, 3, 2, 1]

# Reverse Methods
# list.reverse()
# print(list) #Output [1, 2, 3, 4, 5, 6]

# Insert Methods
# list.insert(3,23)
# print(list) #Output [1, 2, 3, 23, 4, 5, 6]

# Remove Methods
# list.remove(2)
# print(list) #Output [1, 3, 23, 4, 5, 6]

# Pop Methods
# list.pop(3)
# print(list) #Output [1, 3, 23, 5, 6]

#-----------------------------------------------------------------------------------------------------------------------------------------

# Tuples in Python
#Tuple is an built in datatype that lets us create immutable sequeneces
# tuple = (2 ,3, 4, 5, 5)
# print(tuple)
# print(tuple[1:3])
#-----------------------------------------------------------------------------------------------------------------------------------------

# tuple = ()
# print(tuple)
#This is an empty tuple
#-----------------------------------------------------------------------------------------------------------------------------------------

# Tuple methods
# tuple = (2, 4, 5, 21, 2, 1)

# Index Methods
# print(tuple.index(4))

# Count methods
# pront(tuple.count(2))
#-----------------------------------------------------------------------------------------------------------------------------------------

# question 
# Write a program to ask the users to enter names of their 3 favorite moveies and store them in  a list
# str1 = (input("Enter the name of the first movie"))
# str2 = (input("Enter the name of the second movie"))
# str3 = (input("Enter the name of the third movie"))

# list = []
# list.append(str1)
# list.append(str2)
# list.append(str3)

# print(list)
#-----------------------------------------------------------------------------------------------------------------------------------------


#Write a program to check if a list containa palindrome of element.
# Palindrome = [1, 2, 3, 2, 1]
# Palindrome.copy()
# Palindrome.reverse()
# print(Palindrome)

#-----------------------------------------------------------------------------------------------------------------------------------------

#Write a programme to count the number of students with the "A" grafe in the following typr
# ["C", "D", "A", "A", "B", "B", "A"]

grade = ["C", "D", "A", "A", "B", "B", "A"]
print(grade.count("A"))