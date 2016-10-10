def counteven(N):
	count = 0
	for i in range(1, N + 1):
		if i % 2 == 0:
			count += 1
	return count
a = 10
print(counteven(a))