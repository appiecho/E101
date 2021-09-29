#(lab8/numlist.py) Create a program in the lab8 directory that uses a while loop to collect integers as input from the user until a "q" is received 
# provide a text prompt to the user only one time for the data at the beginning. 
# For each integer, use the input() function without specifying a prompt string. 
# The numbers must be appended to a list named numbers.  
#Once all of the numbers have been received, use a for loop to iterate through the list and determine the parameters listed below. 
#Low value 
#High Value
#Sum of the integers in the list
#Print the 3 parameters above along with the total number of integers and the average of the values. Also print the list.  
import math
import sys

numbers = []
max = 0
min = 0
total = 0

while (1 == 1):
  x = input("Enter an integer, enter 'q' to quit: ")
  if x == str("q"):
    break
  else:
    x = int(x)
    numbers.append(x)
    if (min < x > max):
      max = x
    if (min > x < max):
      min = x
print("High value: ", max, "Low value: ", min)

#Sum() function doesn't work, had to use for loop. 
for ele in range(0, len(numbers)):
    total = total + numbers[ele]
print("Sum: ", total)

num_int = len(numbers)
print("Total integers: ", num_int)

avg = total / len(numbers)
print("Average: ", avg)

print(numbers)
