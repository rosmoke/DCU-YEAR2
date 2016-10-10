import sys
words = sys.argv[1:]
line = ":"
for word in words:
	line = line + word + ":"
print(line)