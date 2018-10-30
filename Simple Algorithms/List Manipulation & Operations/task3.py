filename = 'TableNumbers1.txt'
infile = open(filename, 'r')
table = []
for line in infile:
	line = line.split()
	table.append(line)
print(table)
