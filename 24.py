counter = 0
target = 1000000

def p24(set, permutation):
	
	if len(set) == 1:
		global counter
		global target
		counter += 1
		
		if counter == target:
			print(permutation + set[0])
		
		return
	
	for digit in set:
		newSet = set.copy()
		newSet.remove(digit)
		p24(newSet, permutation + digit)
		
p24(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], "")