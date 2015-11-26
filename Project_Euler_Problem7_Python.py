# Project Euler - Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def countPrime(n):
	num = 14
	primes = [2,3,5,7,11,13]

	while len(primes) < n:
	
		haveFactor = False
		for x in primes:
			if num%x == 0:
				haveFactor = True
				break
		if haveFactor == False:
			for i in range(3,num):
				if num%i == 0:
					haveFactor = True
					break

		if haveFactor == False:
			primes.append(num)
		
		print(len(primes))
		
		num += 2


	return primes[n]

print(countPrime(10001))
