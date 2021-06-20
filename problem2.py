#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

num1 = input("enter a number: ")
num2 = input("enter a number: ")
num1 = int(num1)
num2 = int(num2)
if num1>num2:
    big = num1
    small = num2
else:
    small = num1
    big = num2
if (big % small) == 0:
    print(str(small) + " is a factor of " + str(big))
else:
    print(str(small) + " is not a factor of " + str(big))