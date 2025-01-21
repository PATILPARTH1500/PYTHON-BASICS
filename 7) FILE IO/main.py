#PYTHON CAN BE USED TO  PREFORM OPERATIONS ON A FILE ( READ & WRITE DATA)
#TYPES OF FILES
#TEXT FILES :- .txt, .docx, .log etc
#BINARY FILES :- .mp4, .mov, .png, .jpeg etc
#------------------------------------------------------------------------------------------------------------------------------------------

#READ ONLY
# file = open("0) ASSETS\sample.txt", "r")
# data = file.read()
# print(data)#Output I am learning python
# print(type(data)) #Output <class 'str'>
# file.close() #Always close the file to avoid threat in the document
#------------------------------------------------------------------------------------------------------------------------------------------

#READLINE 
# file = open("0) ASSETS\sample.txt" , "r")
# data = file.readline()
# print(data) #Output I am learning python ( in the output it gives extra line space /n)
# file.close()
#------------------------------------------------------------------------------------------------------------------------------------------

#READ ONLY BUT WITH THE CHARACTERS YOU WANT
# file = open("0) ASSETS\sample.txt", "r")
# data = file.read(5)
# print(data)#Output I 
# print(type(data)) #Output <class 'str'>
# file.close()
#------------------------------------------------------------------------------------------------------------------------------------------

#WRITING TO A FILE
# file = open("0) ASSETS\sample.txt", "w")
# file.write("I am also learngin c#")
# file.close
#THIS FUNCTION CHANGES THE EXISTING FILE 
#------------------------------------------------------------------------------------------------------------------------------------------

# #APPEND TO A FILE
# file = open("0) ASSETS\sample.txt", "a")
# file.write("\nI am learning python")
# file.close
#------------------------------------------------------------------------------------------------------------------------------------------

#DELETING FILE
# import os
# os.remove("write your file name")
#------------------------------------------------------------------------------------------------------------------------------------------

#QUIZ
#1) CREATE A NEW FILE "practice.txt" using python Add the following data in it:
#Hi everyone
#we are learning File I/O
#using Java
#I like programming in Java

# file = open("practice.txt", "w")
# file.write("Hi everyone\nwe are learning File I/O\n")
# file.write("using Java\n I like programming in Java")
# file.close
#------------------------------------------------------------------------------------------------------------------------------------------

#WRITE A FUNCTION THAT REPLACE ALL THE OCCURENCE OF "Java" with "Python"
# with open("practice.txt", "r") as file:
#     data = file.read()

# new_data = data.replace("Java", "Python")
# print(new_data)
#------------------------------------------------------------------------------------------------------------------------------------------

#WRITE A FUNCTION THAT FINDS THE "learning" WORD IN THE "practice,txt"
# with open("practice.txt", "r") as file:
#     data = file.read()

# new_data = data.find("learning")
# print(new_data)
#------------------------------------------------------------------------------------------------------------------------------------------


def check_by_line():
    word = "learning"
    data = 