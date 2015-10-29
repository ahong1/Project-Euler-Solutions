# Project Euler - Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def twenty_div1():
	#Since certain numbers from 11 to 20 have  non prime factors 1-10,
	#We don't need to include those numbers in the list
	factors = [11,13,14,16,17,18,19,20]
	#So we ensure that our number is also a multiple of 1-10
	for i in range(2520, 999999999, 2520):
		if all(i%n==0 for n in factors):
			return i

print(twenty_div1())

	
