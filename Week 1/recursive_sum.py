def sumto(a, b, total=0):
	if a == b:
		return(total)
	else:
		total += a
		a += 1
		return(sumto(a, b, total))