# Project Euler - Problem 4
# Question
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largePal():

	#Highest possible value for a product of two 3 digit numbers
	i = 999*999
	
	isPal = False
	
	while isPal == False and i > 10000:
		i = str(i)
		#if i has even number of digits
		if len(i)%2 == 0:
			last_half = i[int(len(i)/2):]
			#Rearranging the order of the digits ----> Will generalize later
			n_last_half = last_half[2] + last_half[1] + last_half[0]
			#if number is a palindrome number
			if i[:int(len(i)/2)] == n_last_half:
				
				#if pal is a product of two 3 digit numbers
				#will terminale while loop if condition is satisfied
				for x in range(999,101,-1):
					if int(i)%x == 0:
						if int(i)//x >=100 and int(i)//x <=999:
							isPal = True
							return i

		#if i has an odd number of digits
		else:
			last_half = i[int(len(i)//2 + 1):]
			for x in range(len(last_half)-1):
				last_half = last_half[1:] + last_half[0]
			
			
			#if number is a palinedrome number
			if i[:int(len(i)//2)] == last_half:
				
				#if pal is a product of two 3 digit numbers
				for x in range(999,101,-1):
					if int(i)%x == 0:
						if int(i)//x >=100 and int(i)//x <-999:
							isPal = True
							return i
		i = int(i)-1

print(largePal())


