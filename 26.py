def p26(limit):
	
	max_divisor = 0
	max_decimal = ""
	max_length = 0

	for divisor in range(2, limit):
			
		dividend = 10
		dividends = []
		decimal = "0."
		length = 0
		
		while dividend / divisor < 1:
			dividend *= 10
			dividends.append(0)
			decimal = decimal + "0"
		
		while dividend != 0 and dividend not in dividends:
			
			dividends.append(dividend)
			decimal = decimal + str(dividend // divisor)
			dividend = dividend % divisor * 10
			
			while dividend / divisor < 1 and dividend != 0:
				dividend *= 10
				dividends.append(0)
		
		if dividend != 0 and (len(dividends) - dividends.index(dividend)) > max_length:
			max_divisor = divisor
			max_decimal = decimal
			max_length = (len(dividends) - dividends.index(dividend))
		
	print(max_divisor)
	print(max_decimal)
	print(max_length)
	
p26(1000)