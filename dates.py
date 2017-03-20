with open('dates', 'r') as f:
	lines = f.read()

lines = lines.split("\n")
print(list(set(lines)))