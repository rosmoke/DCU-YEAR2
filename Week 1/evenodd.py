import sys
word = sys.argv[1]

if len(word) % 2 == 0:
	print(word[(int(len(word)/2)):])
elif len(word) == 1:
	print(word+word)
else:
	print(word[0] + word[-1])