#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
nums = []

for num in range(0,3):
    nums.append(int(input("Enter a number=>")))
nums.sort()
if ((nums[0] ** 2) + (nums[1] ** 2) == (nums[2] ** 2)):
       print(str(nums[0]) + "," + str(nums[1]) + "," +str(nums[2]) +" form a Pythagorean triple")
else:
    print(str(nums[0])
     + "," + str(nums[1]) + "," +str(nums[2]) +" do not form a Pythagorean triple")