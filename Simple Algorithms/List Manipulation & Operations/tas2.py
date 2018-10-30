filename = 'Numbers.txt'
infile = open(filename, 'r')
for contents in infile:
	c = contents.split()
	sum_sqr = 0
	for number in c:
		sum_sqr += float(number) ** 2
	print(sum_sqr)
infile.close()
