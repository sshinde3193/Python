def sumRecursive(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + sumRecursive(L[1:])

L = [2,4,6]
print(sumRecursive(L))
