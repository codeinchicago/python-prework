#Vance Cole's Answers to Python Coding Questions

"""
Question 1
Write a function to print "hello_USERNAME!" 
USERNAME is the input of the function. The first line of the code has been defined as below. 
def hello_name(user_name):

"""

#Answer to Question 1:

def hello_name(user_name):
    print("hello_" + user_name + "!")


#Testing
#hello_name("Me")


"""
Question 2
Question 2
Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
"""

def first_odds():
    for i in range(1,100,2):
        print(i)

#first_odds()

"""
Question 3
Please write a Python function, max_num_in_list to return the max number of a given list. 
The first line of the code has been defined as below. def max_num_in_list(a_list):
"""

def max_num_in_list(a_list):
    max_num = a_list[0]
    for i in a_list[1:]:
        #If a number is larger than the previous maximum number, make it the new maximum.
        if i > max_num:
            max_num = i

    #print(max_num)    
    return max_num

#Testing
#testing = [11,12,10,5,9,1,10,-2,8]
#max_num_in_list(testing)

def is_leap_year(a_year):
    #Divisible by 4
    if a_year % 4 == 0:
        #Check for divisible by 100
        if a_year % 100 != 0:
            #print("True.")
            return True
        if a_year % 100 == 0:
            #Check for divisibility by 400.
            if a_year % 400 == 0:
                #print("True.")
                return True
            else:
                #print("False.")
                return False


    #All other cases are not leap years.
    else:
        #Testing
        #print("False.")
        return False


#Testing
#a_year = 1995
#a_year = 1872
#a_year = 1998
#a_year = 2000
#a_year = 2000.1
#a_year = 2004
#a_year = 1900
#is_leap_year(a_year)

"""
Question 5

Write a function to check to see if all numbers in the list are consecutive numbers. 
For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
The return should be boolean Type. def is_consecutive(a_list):
"""

def is_consecutive(a_list):
    consecutive_number = a_list[0]
    for i in a_list:
        #Checking if number is consecutive
        if i == (consecutive_number + 1):
            consecutive_number = i
        else:
            #print("False.")
            return False
    #If no numbers are not consecutive, all are consecutive.
    #print("True.")
    return True

#True test case.
#test = [2,3,4,5,6,7]
#False test cases.
#test = [1,2,3.1]
#test = [1,2,3,5]
#is_consecutive(test)