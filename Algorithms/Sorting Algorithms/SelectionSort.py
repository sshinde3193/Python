aList = [5, 2, 1, 5, 2, 3]

def selectionsort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            if aList[k] < aList[least]:
                least = k
        print(aList)
        swap(aList, least, i)

def swap(aList, i, j):
    aList[i], aList[j] = aList[j], aList[i]

selectionsort(aList)
