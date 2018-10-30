aList = [5, 2, 1, 5, 2, 3]

def bubble_sort(aList):
    no_swaps = True
    for mark in range(len(aList) - 1, 0, -1):
        for j in range(mark):
            if aList[j] > aList[j+1]:
                no_swaps = False
                swap(aList, j, j+1)
        if no_swaps:
            break
        no_swaps = True
    return aList

def swap(aList, i, j):
    aList[i], aList[j] = aList[j], aList[i]

print(bubble_sort(aList))
