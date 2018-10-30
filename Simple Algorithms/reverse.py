lst = [1, 2, 3, 4]

for i in range(-1, -len(lst)-1, -1):     # for loop method
    print(lst[i])

while lst != []:              # Stack method
    x = lst.pop()
    print(x)
