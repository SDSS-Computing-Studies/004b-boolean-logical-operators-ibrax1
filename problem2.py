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
small = input("enter a small number: ")
big = input("enter a bigger number: ")
big = int(big)
small = int(small)

if (big % small) == 0:
    print(str(small) + " is a factor of " + str(big))
else:
    print(str(small) + " is not a factor of " + str(big))