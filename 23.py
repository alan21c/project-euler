import math

def find_divisors(num):
	divisors = [1]
	
	for x in range(2, math.ceil(math.sqrt(num))):
		if(num % x == 0):
			divisors.append(x)
			divisors.append(int(num/x))
	
	if (math.isqrt(num) ** 2 == num):
		divisors.append(math.isqrt(num))
	
	return divisors
	

def is_abundant(num):
	return sum(find_divisors(num)) > num


def find_abundant_numbers(limit):
	abundant_numbers = []

	for x in range(2, limit, 2):
		if(is_abundant(x)):
			abundant_numbers.append(x)
	
	for x in range(3, limit, 6):
		if(is_abundant(x)):
			abundant_numbers.append(x)

	return abundant_numbers	


def p23():
	non_abundant_sums = []
	abundant_numbers = find_abundant_numbers(28123)
	
	for x in range(28124):
		non_abundant_sums.append(x);	
		
	for x in abundant_numbers:
		for y in abundant_numbers:
			try: 
				non_abundant_sums[x + y] = 0; #faster than list.remove()
			except IndexError:
				pass
	
	print(sum(non_abundant_sums))
	

p23();