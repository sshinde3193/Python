a_sorted = [1,1,2,3,4,5,5,5,5,6,9,9]

def duplicate(a_sorted):
    L = []
    for i in range(len(a_sorted)):
        for j in range(i+1, len(a_sorted)):
            if a_sorted[i] == a_sorted[j]:
                L.append(a_sorted[j])

            for k in range(len(L)):
                for a in range(k + 1, len(L)):
                    if L[k] == L[a]:
                        L.pop(a)
    return L

print(duplicate(a_sorted))
