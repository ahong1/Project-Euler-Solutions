#Project Euler = Problem 1

#Problem
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Solution:

def sum_of_3_5(num):
	sum = 0
	for i in range(num):
		if i%3 == 0:
			sum = sum + i
		elif i%5 == 0:
			sum = sum + i
	return sum

print(str(sum_of_3_5(1000)))

# Result - Correct
# Notes:
# good easy warm up.