name = input('Enter a word: ')
name_length = len(name)
print('The length of the name is %s' %name_length)

# 5 chars, therfore 5 char counts.

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Loop through name and increment count each time a char is found respectively.

for char in name:
	if 'a' == char:
		count_a += 1
	if 'e' == char:
		count_e += 1
	if 'i' == char:
		count_i += 1
	if 'o' == char:
		count_o += 1
	if 'u' == char:
		count_u += 1

print('The number of a\'s in name are ' + str(count_a))
print('The number of e\'s in name are ' + str(count_e))
print('The number of i\'s in name are ' + str(count_i))
print('The number of o\'s in name are ' + str(count_o))
print('The number of u\'s in name are ' + str(count_u))
