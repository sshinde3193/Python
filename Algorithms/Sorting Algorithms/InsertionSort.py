aList = [5, 2, 1, 5, 2, 3]

def insertion_sort(aList):
    for mark in range(1, len(aList)):
        current_value = aList[mark]
        position = mark - 1

        while position >= 0 and aList[position] > current_value:
            aList[position + 1] = aList[position]
            position -= 1

        aList[position + 1] = current_value
    return aList

print(insertion_sort(aList))
