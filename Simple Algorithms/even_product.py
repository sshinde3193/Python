target = 65
L = [2,5,4,1,7,2,4] # product of even numbers is 64

def even_prod(target, L):
    prod = 1
    result = False
    for i in range(len(L)):
        if L[i] % 2 == 0:
            prod = prod * L[i]

    if prod > target:
        result = True

    return result

print(even_prod(target, L))
