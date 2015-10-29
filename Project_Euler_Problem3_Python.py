# Project Euler - Problem 3

# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Solution:

def high_factor(num):
	i = 2
	factors = []
	while num > 1:
		if num%i == 0:
			factors.append(i)
			num/=i
		i = i +1
	return factors

	
print(str(max(high_factor(600851475143))))

				
# Result - Correct
# Notes:
# Kept getting an infinite loop when i tried to implement a while loop
# Learned the process of prime factorization and tried to implement it
# in the least number of iterations