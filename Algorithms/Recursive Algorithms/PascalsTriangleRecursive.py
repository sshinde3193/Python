# The printPascal function prints the Pascal triangle recursively.
# The function takes two parameters, List L and n as the number of rows that still need to be printed in the Triangle.
# The nextPascal function is called in the printPascal function to get the next row of the Pascal's triangle

def printPascal(L, n):
    if len(L) == 0:
        L.append([1])                                 # First base case: [1] is put into the list if the list is empty
        print(*L[0])                                  # The zeroth index of the list is printed which prints [1]
        if n == 0:
            return
        printPascal(L, n)
    elif n == 1:                                       # Second base case: when n equals 1, the zeroth and first row need to be printed
        L.append([1, 1])                               # Therefore, we put [1,1] into the first row
        print(*L[1])                                   # The first index of the list is printed which prints [1,1]
        return L[1]
    else:
        previous = printPascal(L, n-1)
        if n > 1:
            i = 0                                               # 'i' is the counter variable for the current line
            print(*nextPascal(previous, i))                     # Prints the next row of the Pascal's Triangle
            L.append(nextPascal(previous, i))                   # Updates the List L to contain the next row in the Pascal's triangle
            return nextPascal(previous, i)

# This function returns the nextRow of the Pascal Triangle recursively.
# This function takes two parameters, the previous row and the counter variable 'i'
# This function is called in the PrintPascal function to print the next row

def nextPascal(prev_row, i):
    if i == 0:                                                      # First base case, when 'i' is at the zeroth position, [1] is inserted into the list
        return [1] + nextPascal(prev_row, i+1)                      # And i increases by 1 and recursively calls itself

    elif i == len(prev_row):                                        # Second base case, when 'i' equals the length of the previous row we return [1]
        return [1]

    else:
        curr_pos = [prev_row[i - 1] + prev_row[i]]
        return curr_pos + nextPascal(prev_row, i+1)


L = []
n = int(input('Enter a non-negative integer n: '))
printPascal(L, n)
