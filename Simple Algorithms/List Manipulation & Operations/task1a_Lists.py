numbers = input('Enter some numbers: ')

numbers = numbers.split()								# Stores the numbers in a list

for i in range(len(numbers)):
	numbers[i] = int(numbers[i])						# converts each element in list from string to integer

print(numbers)
