def BinarySearch(aList, target):
    low = 0
    high = len(aList)-1
    while low <= high:
        mid = (low + high) // 2
        if aList[mid] == target:
            return True
        elif aList[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return False

aList = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(BinarySearch(aList, 17))
