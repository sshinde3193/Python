aList = [5, 2, 1, 5, 2, 3]

def bubbleSort(aList):
    for i in range(len(aList) - 1):
        for j in range(len(aList) - 1):
            if aList[j] > aList[j + 1]:
                swap(aList, j, j + 1)
    return aList

def swap(aList, i, j):
    aList[i], aList[j] = aList[j], aList[i]

print(bubbleSort(aList))
