def rprint(a, b):
	if a == b:
		return
	else:
		print(a)
		a = a + 1
		rprint(a, b)