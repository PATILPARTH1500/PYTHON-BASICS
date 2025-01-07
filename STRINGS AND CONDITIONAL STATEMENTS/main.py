# Different quotes are use to define strings in Python and
# to avoid apostrophe issues, we can use double quotes or triple quotes.
# str1 = "This is a string"
# str2 = 'This is also a string'
# str3 = """This is a string with triple quotes"""
#---------------------------------------------------------------------------------------------------------------------------------------------

# Escape characters in Python
# str1 = "Hello\nWorld"
# print(str1)

# str2 = "Hello\tWorld"
# print(str2)
#---------------------------------------------------------------------------------------------------------------------------------------------

# Concatenation of strings
# str1 = "Hello"
# str2 = "World"
# str3 = str1 + str2
# print(str3)
#---------------------------------------------------------------------------------------------------------------------------------------------

# Length of the strings
# str1 = "Hello World"
# print(len(str1)) # Output: 11
# final = str1 + "" 
# print(len(final)) # Output: 12
#---------------------------------------------------------------------------------------------------------------------------------------------

# Indexing in strings
# P A R T H  P A T I L 
# 0 1 2 3 4 5 6 7 8 9 10 11
# str1 = "PARTH PATIL"
# print(str1[0]) # Output: P
#WE can't change the value of string using indexing
#---------------------------------------------------------------------------------------------------------------------------------------------

# Slicing in strings
# str1 = "PARTH PATIL"
# print(str1[0:5]) # Output: PARTH
# print(str1[6:11]) # Output: PATIL
# print(str1[:5]) # Output: PARTH
# print(str1[6:]) # Output: PATIL
# print(str1[:]) # Output: PARTH PATIL
#---------------------------------------------------------------------------------------------------------------------------------------------

#Negative indexing in strings
# P A R T H  P A T I L
# -11-10-9-8-7-6-5-4-3-2-1
# str1 = "PARTH PATIL"
# print(str1[-11:-1]) # Output: PARTH PATIL
# print(str1[-11:-6]) # Output: PARTH
# print(str1[-5:]) # Output: PATIL
# print(str1[:-6]) # Output: PARTH
# print(str1[:-11]) # Output: 
#---------------------------------------------------------------------------------------------------------------------------------------------

#String Functions
str = " I am a coder"

#endswith() function
print(str.endswith("coder")) # Output: True
print(str.endswith("I")) # Output: False

#startswith() function
print(str.startswith(" I")) # Output: True
print(str.startswith("i")) # Output: False

#capitalize() function
print(str.capitalize()) # Output:  i am a coder

#replace() function
print(str.replace("coder", "programmer")) # Output: I am a programmer

#find() function
print(str.find("coder")) # Output: 7

#count() function
print(str.count("m")) # Output: 1

#------------------------------------------------------------------------------------------------------------------------------------------------

#commmit
