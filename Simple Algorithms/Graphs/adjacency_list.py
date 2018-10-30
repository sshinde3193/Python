filename = 'testGraph.txt'
infile = open(filename, 'r')							# Each line of the file has exactly one edge reprsented by 2 vertices
n = int(input('Enter the number of vertices: '))

table = []
for line in infile:
	line = line.split()
	for i in range(len(line)):
		line[i] = int(line[i])
	table.append(line)

adj_list = []
for i in range(len(table)):
	vertex = []
	for u,v in table:
		if u == i:
			vertex.append(v)
		elif v == i:
			vertex.append(u)
	adj_list.append(vertex)

print(adj_list)
