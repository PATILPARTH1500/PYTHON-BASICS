#LOOPS IN PYTHON 

#WHILE LOOP PYTHON 
#---------------------------------------------------------------------------------------------------------------------------------------------


#INFINITY LOOP USING WHILE LOOP
#THIS WILL CRASH OUR WEBSITE OR TERMINAL
# while(True):
    # print("Hi") 
#---------------------------------------------------------------------------------------------------------------------------------------------

# #WHILE LOOP 
# i = 1
# while(i <= 5):
#     print("Hello World" , i)
#     i = i + 1
    
# print(i) #Output 6
#---------------------------------------------------------------------------------------------------------------------------------------------

#QUIZ
#Print numbers from 1 to 100.
# i = 1
# while(i <= 100):
#     print(i)
#     i = i + 1
#---------------------------------------------------------------------------------------------------------------------------------------------

#Print numbers from 100 to 1
# i = 100
# while(i >= 1):
#     print(i)
#     i -= 1
#---------------------------------------------------------------------------------------------------------------------------------------------
 
#Print the multiplication table of a number n 
# n = int(input("enter the number"))
# i = 1
# while(i <=10):
#     print(i * n)
#     i += 1
#---------------------------------------------------------------------------------------------------------------------------------------------

#Print the elements of the following list using a loop 
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 1
# while(i <= 10):
#     print(i * i)
#     i += 1
#---------------------------------------------------------------------------------------------------------------------------------------------

#Search for a number x in this tuple using loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# tup = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 25
# i = 1
# while i < len(tup):
#     if(tup[i] == x):
#         print("Found at index", i )
#     i +=1 
#---------------------------------------------------------------------------------------------------------------------------------------------

#BREAK AND CONTINUE KEY WORD IN LOOPS
#BREAK :- BREAK KEYWORD IS USED TO TERMINATE THE LOOP 

# tup = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = 8
# i = 1
# while i < len(tup):
#     if(tup[i] == x):
#         print("Founded at index" , i)
#         break
#     else:
#         print("finding....")
#     i += 1
#---------------------------------------------------------------------------------------------------------------------------------------------

#CONTINUE :- CONTINUE KEYWORD IS USED TO TERMINATE EXECUTION IN THE CURRENT ITERATION & CONTINUES EXECUTION OF THE LOOPS WITH THE NEXT ITERATION

# i = 1
# while(i<=5):
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1 this statement will not show the output 3 because after the continue the all the statements are skipped and again the loop has started
#---------------------------------------------------------------------------------------------------------------------------------------------

#FOR LOOP IN PYTHON 

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for values in nums:
#     print(values)
#---------------------------------------------------------------------------------------------------------------------------------------------

# str =  "ParthPatil"

# for char in str:
#     if(char == "i"):
#         print("Founded at index")
#         break
#     print(char)
# else:
#     print("Loop ended")
#---------------------------------------------------------------------------------------------------------------------------------------------

#RANGE()
#RANGE :- RANGE FUNCTION RETURNS A SEQUENCE OF NUMBERS STARTING FROM 0 BY DEFAULT AND INCREMENTS BY 1 BY DEFAULT AND STOPS BEFORE A 
#SPECIFIED NUMBERS.

# for value in range(5): #end value
#     print(value)
# #---------------------------------------------------------------------------------------------------------------------------------------------

# for value in range(1, 5): #start value and end value
#     print(value)
# #---------------------------------------------------------------------------------------------------------------------------------------------
    
# for value in range(2, 10 , 2): #start value , end value and step up value
#     print(value)
#---------------------------------------------------------------------------------------------------------------------------------------------

