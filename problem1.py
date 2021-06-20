"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3
divisibleby6 = False
divisibleby8 = False
input = input("Enter a number: ")
input = int(input)
if (input % 6) == 0 and (input % 8) != 0:
    divisibleby6 = True
    print(str(input) + " is frue")
else:
    print(str(input) + " is not frue")
