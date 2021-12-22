# Assignment 6

# Program 1: Number Sorter
# Create a program that ask 4 numbers.
# Print the 4 numbers from highest to lowest using only if-else statement.

# input
# sort
# print

def getInput():
    global n1,n2,n3,n4
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))
    n3 = int(input("Enter the 3rd number: "))
    n4 = int(input("Enter the 4th number: "))

def numSorter():
    global first, second, third, fourth #declare the variables for storing the sorted numbers
    
    # the goal is to sort the n1 and n2 first. Then put the n3 in new arrangement
    # lastly, print the numbers from fourth to first number

    if n1 <= n2:                               # sort the first two numbers
        first = n1                             #
        second = n2                            #    

        if n3 < n1:                                 # sort with third number
            first = n3                              #
            second = n1                             #
            third = n2                              #

            if n4 < n3:                                 # sort with fourth number
                first = n4                              #
                second = n3                             #
                third = n1                              #
                fourth = n2                             #
            elif n4 >= n3 and n4 <= n1:                 #
                first = n3                              #
                second = n4                             #
                third = n1                              #
                fourth = n2                             #
            elif n4 >= n1 and n4 <= n2:                 #
                first = n3                              #
                second = n1                             #
                third = n4                              #
                fourth = n2                             #
            elif n4 > n2:                               #
                first = n3                              #
                second = n1                             #
                third = n2                              #
                fourth = n4                             # 
            

        elif n3 >= n1 and n3 <= n2:                 
            first = n1
            second = n3
            third = n2

            if n4 < n1:                                 # sort with fourth number
                first = n4                              #
                second = n1                             #
                third = n3                              #
                fourth = n2                             #
            elif n4 >= n1 and n4 <= n3:                 #
                first = n1                              #
                second = n4                             #
                third = n3                              #
                fourth = n2                             #
            elif n4 >= n3 and n4 <= n2:                 #
                first = n1                              #
                second = n3                             #
                third = n4                              #
                fourth = n2                             #
            elif n4 > n2:                               #
                first = n1                              #
                second = n3                             #
                third = n2                              #
                fourth = n4                             # 

        elif n3 > n2:
            first = n1
            second = n2
            third = n3

            if n4 < n1:                                 # sort with fourth number
                first = n4                              #
                second = n1                             #
                third = n2                              #
                fourth = n3                             #
            elif n4 >= n1 and n4 <= n2:                 #
                first = n1                              #
                second = n4                             #
                third = n2                              #
                fourth = n3                             #
            elif n4 >= n2 and n4 <= n3:                 #
                first = n1                              #
                second = n2                             #
                third = n4                              #
                fourth = n3                             #
            elif n4 > n2:                               #
                first = n1                              #
                second = n2                             #
                third = n3                              #
                fourth = n4                             # 

    else:                                     # sort the first two, this separate the path of sorting algo
        first = n2
        second = n1

        if n3 < n2:                                 # sort with third
            first = n3
            second = n2
            third = n1

            if n4 < n3:                                 # sort with fourth number
                first = n4                              #
                second = n3                             #
                third = n2                              #
                fourth = n1                             #
            elif n4 >= n3 and n4 <= n2:                 #
                first = n3                              #
                second = n4                             #
                third = n3                              #
                fourth = n1                             #
            elif n4 >= n2 and n4 <= n1:                 #
                first = n3                              #
                second = n2                             #
                third = n4                              #
                fourth = n1                             #
            elif n4 > n1:                               #
                first = n3                              #
                second = n2                             #
                third = n1                              #
                fourth = n4                             # 

        elif n3 >= n2 and n3 <= n1:
            first = n2
            second = n3
            third = n1

            if n4 < n2:                                 # sort with fourth number
                first = n4                              #
                second = n2                             #
                third = n3                              #
                fourth = n1                             #
            elif n4 >= n2 and n4 <= n3:                 #
                first = n2                              #
                second = n4                             #
                third = n3                              #
                fourth = n1                             #
            elif n4 >= n3 and n4 <= n1:                 #
                first = n2                              #
                second = n3                             #
                third = n4                              #
                fourth = n1                             #
            elif n4 > n1:                               #
                first = n2                              #
                second = n3                             #
                third = n1                              #
                fourth = n4                             # 

        elif n3 > n2:
            first = n2
            second = n1
            third = n3

            if n4 < n2:                                 # sort with fourth number
                first = n4                              #
                second = n2                             #
                third = n1                              #
                fourth = n3                             #
            elif n4 >= n2 and n4 <= n1:                 #
                first = n2                              #
                second = n4                             #
                third = n1                              #
                fourth = n3                             #
            elif n4 >= n1 and n4 <= n3:                 #
                first = n2                              #
                second = n1                             #
                third = n4                              #
                fourth = n3                             #
            elif n4 > n1:                               #
                first = n2                              #
                second = n1                             #
                third = n3                              #
                fourth = n4                             # 


def printAll():
    
    print("Sorted numbers:")
    print("1st: " + str(fourth))
    print("2nd: " + str(third))
    print("3rd: " + str(second))
    print("4th: " + str(first))

getInput()
numSorter()
printAll()