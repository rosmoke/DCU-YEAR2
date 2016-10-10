from Stack import Stack

def reverse_input(stack):
	line = input()
	while line:
		stack.push(line)
		line = input()
	while not stack.is_empty():
		print(stack.pop())

reverse_input(stack)