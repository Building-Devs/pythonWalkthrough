# A code generating prime numbers
# First 50
# Prime Number: 1 2 3 5 7 11 13 17 19

# if statement
def primeNum(max):
	""" 
	A function to generate the first n prime numbers.
	input: number. The nth number. Type: integer
	ouput: prime_list. List of n prime numbers. Type: list
	"""

	prime_list = [1]
	for num in range(1, max+1):
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					break
			else:
				prime_list.append(num)
				
	return prime_list

number = int(input("Please enter the number of prime numbers you want: "))


print(primeNum(number))
