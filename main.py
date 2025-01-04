# Print Statement
# Print statement is used to print the output on the screen.
# print("Hello World")
# print("Parth")
# print("My age is 18.", "I am a student.")
# print(15)
# print(15.5)
# print(1-2)
#---------------------------------------------------------------------------------------------------------------------------------------------

# Variables Statement
# Variable is a container to store data values.
# name="Parth"
# age=18
# marks=90.5
# age2=age
# print(age2)
# print(name, age, marks)
#---------------------------------------------------------------------------------------------------------------------------------------------

# Rules for variable
# 1. A variable name must start with a letter or the underscore character.
# 2. A variable name cannot start with a number.
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# 4. Variable names are case-sensitive (name, Name and NAME are three different variables).
# 5. Variable names should be descriptive and meaningful.
# 6. Variable names should not be a keyword.
# 7. Variable names should not contain any special character(&,%,$,#,@ etc).
#---------------------------------------------------------------------------------------------------------------------------------------------

# Variable Types
# name="Parth" #String <class 'str'>
# age=18 #Integer <class 'int'>
# marks=90.5 #Float <class 'float'>
# is_student=True #Boolean <class 'bool'>
# none=None #None <class 'NoneType'>
# print(type(name))
# print(type(age))
# print(type(marks))
# print(type(is_student))
#---------------------------------------------------------------------------------------------------------------------------------------------

#Keywords
# Keywords are the reserved words in Python.
# False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, 
# global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
#---------------------------------------------------------------------------------------------------------------------------------------------

#Quiz
#SUM
# a=10
# b=20
# sum=a+b
# diff=a-b
# print(diff) #-10
# print(sum)  #30
#---------------------------------------------------------------------------------------------------------------------------------------------

#Type of Tokens
#Punctuators
#Punctuators are the symbols used to separate the tokens in a program.
#{}, (), [], :, ;, ., @, =, ->, +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=, ==, !=, <, >, <=, >=, <<, >>, &&, ||, !, ~, ++, --, ->*, .*,
# ?:, sizeof, new, delete, new[], delete[]
#---------------------------------------------------------------------------------------------------------------------------------------------

#Python is implicitly typed language
#Python is a dynamically typed language, which means that you don't have to declare the type of the variable.
#---------------------------------------------------------------------------------------------------------------------------------------------


#Expression Execution

# 1) String and Numeric values can operate together with *
# a,b=10,20
# Txt="@"
# print(a*Txt) #@@@@@@@@@@
# #---------------------------------------------------------------------------------------------------------------------------------------------

# # 2) String and String values can operate together with +
# a,b="10",20
# Txt="@"
# print((a+Txt)*b) #10@10@10@
# #---------------------------------------------------------------------------------------------------------------------------------------------

# # 3) Numeric values can operatte together with all the arethmetic operators
# a,b=10,20
# c=5
# print(a+b*c) #110
# #---------------------------------------------------------------------------------------------------------------------------------------------

# #4) Arithmetic operators with integers and float will result in float
# a,b=10,20.5
# c=5
# print(a+b*c) #120.5
# #---------------------------------------------------------------------------------------------------------------------------------------------

# #5) Result of division operator is always float
# a,b=10,20
# print(b/a) #2.0
# #---------------------------------------------------------------------------------------------------------------------------------------------

# #7) Integer division with float and int will result in float
# a,b=1.0,20
# c=a//b
# print(c, a/b) #0.0 0.05
# #---------------------------------------------------------------------------------------------------------------------------------------------

# #8) Modulo Expression
# a=10
# b=3
# print(a%b) #1

# a=-10
# b=3
# print(a%b) #2

# a=10
# b=-3
# print(a%b) #-2

# a=-10
# b=-3
# print(a%b) #-1
#---------------------------------------------------------------------------------------------------------------------------------------------

#Comments in python
#Single line comment
"""Multi line comment"""
#---------------------------------------------------------------------------------------------------------------------------------------------

#Input Statement
# name = input("Enter your name: ")
# age = int(input("Enter your age:"))
# marks = float(input("Enter your marks:"))
# print(name, age, marks)
#---------------------------------------------------------------------------------------------------------------------------------------------

#Conditional Statements

#Traffic Light Example
# light = input("enter the color of the light: ")
# if light == "red":
#     print("stop")
# elif light == "yellow":
#     print("wait")
# elif light == "green":  
#     print("go")
# else:
#     print("Error in the input")
#---------------------------------------------------------------------------------------------------------------------------------------------

#Marks Example
# marks = int(input("enter the marks:"))
# if (marks >=90):
#     print("Grade A")
# elif (marks>=80):
#     print("Grade B")
# elif (marks>=70):
#     print("Grade C")
# elif (marks>=60):
#     print("Grade D")
# elif (marks>=50):
#     print("Grade E")
# else:
#     print("Fail")
#---------------------------------------------------------------------------------------------------------------------------------------------

#Quiz
# A = int(input("Enter the value of A: "))
# G = input("M or F: ")
# if((A == 1 or A == 2) and G == "M"):
#     print("fee is 100")
# elif((A == 3 or A == 4 ) and G == "F"):
#     print("fee is 200")
# elif(A == 5 and G == "M"):
#     print("fee is 300")
# else:
#     print("no fee")
#---------------------------------------------------------------------------------------------------------------------------------------------
    
#Single line if else statement
# food = input("Enter the food: ")
# eat = "Yes" if food == "Protein" else "No"
# print(eat)
#---------------------------------------------------------------------------------------------------------------------------------------------

# Food = input("Enter the food: ")
# Eat = "Yes" if Food == "Protein" or Food == "Carbs" else "No"
# print(Eat)
#---------------------------------------------------------------------------------------------------------------------------------------------

#Clever If/ Ternary Operator
# age = int(input("Enter the age: "))
# vote = ("yes" , "no") [age < 18]
# print(vote)
#---------------------------------------------------------------------------------------------------------------------------------------------

# sal = float(input("Enter the salary: "))
# tax = (sal*0.1 , sal*0.2) [sal > 50000] 
# print(tax)
#---------------------------------------------------------------------------------------------------------------------------------------------

# Best Practices in Python
# 1. Simple Instructions
# 2.One Instruction per task
# 3. Use meaningful variable names
# 4. Use comments
# 5. Use white spaces
# 6. Use indentation
# 7. Avoid complex expressions
#---------------------------------------------------------------------------------------------------------------------------------------------

# Calculate the simple interest 
# p = float(input("Enter the principal amount: "))
# r = float(input("Enter the rate of interest: "))    
# t = float(input("Enter the time: "))
# si = (p*r*t)/100
# print(si)
#---------------------------------------------------------------------------------------------------------------------------------------------

#Calculate the area of the circle
# r = float(input("Enter the radius: "))
# area = 3.14*r*r
# print(area)
#---------------------------------------------------------------------------------------------------------------------------------------------

# Types of Operators

# 1. Arithmetic Operators
# + , - , * , / , % , // , **

# 2. Comparison Operators
# == , != , > , < , >= , <=

# 3. Logical Operators
# and , or , not

# 4. Assignment Operators
# = , += , -= , *= , /= , %= , //= , **=
#---------------------------------------------------------------------------------------------------------------------------------------------

# Type Conversion in Pyhton and Type Casting

a = 1
b = 2.0
print(a+b) #3.0
print(type(a+b)) #<class 'float'>
#Python will convert int to float automatically because floar has more precision than int.
#---------------------------------------------------------------------------------------------------------------------------------------------

w = "1"
x = 2   
print(w+x) #Error
#Python will not convert string to int automatically.
#---------------------------------------------------------------------------------------------------------------------------------------------

c = float("1")
d = 2
print(c+d) #3.0
print(type(c+d)) #<class 'float'>
#Type casting is done by the user.
#---------------------------------------------------------------------------------------------------------------------------------------------

