def sum_to_k(lst, k):
	i = 0
	j = 1
	while i < len(lst)-1:
		while j < len(lst):
			if lst[i] + lst[j] == k:
				print(lst[i],lst[j])
				break
			j = j + 1
		i = i + 1
		j = i + 1