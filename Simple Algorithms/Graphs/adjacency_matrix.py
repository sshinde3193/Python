filename = 'testGraph.txt'
infile = open(filename, 'r')
n = int(input('Enter the number of teams: '))
table = []
for line in infile:
	line = line.split()
	for i in range(len(line)):
		line[i] = int(line[i])
	table.append(line)
print(table)

adj_matrix = []
# for i in range(len(table)):
	# vertex = [0] * n
	# for j in range(len(table)):
	# 	if i in table[j]:
	# 		vertex[i][j+1] = 1
	# adj_matrix.append(vertex)
	
	# vertex = [0] * n
	# for u,v in table:
	# 	if u == i:
	# 		index = v
	# 		vertex[u][index] = 1
	# print(vertex)

for i in range(len(table)):
	vertex = [0] * n
	for j in range(len(table)):
		if table[j][i] == i:
			#vertex[i][j + 1] = 1
			for u,v in vertex:
				v = 1
	adj_matrix.append(vertex)


print(adj_matrix)
