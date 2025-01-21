#FUNCTION IN PYTHON
#BLOCK OF STATEMENT THAT PERFORMS A SPECIFIC TASK
#REPEAT = REDUNDANT AVOID WRITING SAME CODE 
#ALWAYS PREFER FUNCTION FOR REDUNDANT THINGS

# def calc_sum(a, b): #defining function 
#     sum = a + b #what is the purpose of the variables in function ?
#     print(sum) #printing sum
#     return sum #shows output
    
# calc_sum(2, 4) #calling function
# calc_sum(4, 1)
# calc_sum(4, 7)

#-------------------------------------------------------------------------------------------------------------------------------------------------
# #function definition
# def calc_sum(a, b): # a & b in the function are called parameters
#     return a+ b

# print(calc_sum(1, 2)) #function calling and values are called arguments

#-------------------------------------------------------------------------------------------------------------------------------------------------
# #No Parameters and Arguments function 
# def print_hello():
#     print("Hello World")

# print_hello()

#-------------------------------------------------------------------------------------------------------------------------------------------------
#Average finding function

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg
# print(calc_avg(1,3,4))

#-------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCTION ARE OF TWO TYPE 
#BUILT-IN :- print() , len(), type(), range()
#USER-DEFINED :- WHICH WILL BE WRITTEN BY PROGRAMMERS

#-------------------------------------------------------------------------------------------------------------------------------------------------
#DEFAULT PARAMETERS

# def calc_prod(a = 3, b = 4): #single value can also be defined to parameters always first values must be user given value
#     print(a * b)
#     return(a * b)

# calc_prod()
# #-------------------------------------------------------------------------------------------------------------------------------------------------
#QUIZ   
#WRITE A PYTHON PROGRAMM TO PRINT THE LENGTH OF A LIST ( LIST IS PARAMETER)

# city = ["Navi-Mumbai", "Delhi", "Pune"]    
# heroes = ["Ironman", "Thor", "Spiderman"]

# def print_len(list):
#     print(len(list))

# print_len(city)
# print_len(heroes)

# def print_list(list):
#     for item in list:
#         print(item, end = " ")
        
# print_list(heroes)
# print_list(city)
# print()
#-------------------------------------------------------------------------------------------------------------------------------------------------
#WRITE A PYTHON PROGRAM TO FIND THE FACTORIAL OF N 
# def fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         print(fact)
        
# fact(8)

#-------------------------------------------------------------------------------------------------------------------------------------------------
#WRITE A PYTHON PROGRAMM TO CONVERT USD TO INR
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print("USD =", usd_val, "INR =", inr_val)

# converter(20)

#-------------------------------------------------------------------------------------------------------------------------------------------------
#WRITE A FUNCTION TO IDENTIFY WHETER THE NUMBER IS EVEN OR ODD
# def num(a, b):
    
#     if(a%b == 0 ):
#         print("EVEN")
#     else:
#         print("ODD")

# num(4, 2)
#-------------------------------------------------------------------------------------------------------------------------------------------------

#RECURSION
#WHEN A FUNCTION CALLS ITSELF REPEATEDLY

# def show(n):
#     if(n == 0):
#         return #Base case
#     print(n)
#     show(n-1)
#     print("end")
# show(6)
# #-------------------------------------------------------------------------------------------------------------------------------------------------

# # #RECURENSE RELATION
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     else:
#         return n * fact(n -1)
    
# print(fact(7))

# #-------------------------------------------------------------------------------------------------------------------------------------------------
# #QUIZ
# #WRITE A PYTHON RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS
# def calc_num(n):
#     if(n == 0):
#         return 0
#     return calc_num(n - 1) + n

# print(calc_num(8))

#-------------------------------------------------------------------------------------------------------------------------------------------------
