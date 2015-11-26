# Project Euler - Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(list1):
	square_list = []
	sum_square = 0

	for i in list1:
		x = i**2
		square_list.append(x)
		sum_square = sum_square + square_list[i]

	
	sum_nat = 0
	for n in list1:
		sum_nat = sum_nat + n
	
	sum_nat = sum_nat**2
	
	return sum_nat - sum_square

list1 = list(range(0,101))
print(sum_square_difference(list1))