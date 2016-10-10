def is_palindrome(word, i = 0, j = 0, times = 0, palindrome = False):
	if len(word) < 2:
		return(True)
	elif len(word)%2 == 0: #even words
		if times == 0:
			i = int(len(word) / 2)
			j = i - 1
		if times < int(len(word) / 2) and word[i] == word[j]:
			i = i + 1
			j = j - 1
			times += 1
			return(is_palindrome(word, i, j, times, True))
		if times >= int(len(word) / 2):
			return(True)
		else:
			return(False)
	else: #odd words
		if times == 0:
			i = int(len(word)/2) + 1
			j = i - 2
		if times < int(len(word) / 2) and word[i] == word[j]:
			i = i + 1
			j = j - 1
			times += 1
			return(is_palindrome(word, i, j, times, True))
		if times >= int(len(word) / 2):
			return(True)
		else:
			return(False)