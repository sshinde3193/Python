filename = input('Enter the filename: ')            # Asks the user which file to open
infile = open(filename, 'r')                        # Opens the file requested by the user
contents = infile.readlines()                       # Reads the contents of the file
infile.close()                                      # Closes the file after the contents have been read.

magicSum = int(input('Enter the magicSum value: '))     # User inputs the value which each row, column and diagonals at the most add upto respectively.

partialMagicSquare = []                                 # Sets magic square equal to an empty list

for i in range(len(contents)):
    row = contents[i].split()                   # Splits the entire string resulting in each number to act as an individual string while being a part of lists
    for j in range(len(contents)):
        row[j] = int(row[j])                    # Converts each individual string number in a list into an integer value
    partialMagicSquare.append(row)              # This inserts the set of integer values as lists into the empty list partialMagicSquare

cont = True                                     # cont is a variable which is actually represents continue
while (cont):                                   # while loop runs unless the user stops the program

    print("Do you want to stop the program? Yes or No")
    ans = input('Answer: ')

    if ans == "Yes":
        cont = False

    elif ans == "No":
        for line in partialMagicSquare:         # It's printing the magic square (row in each separate line)
            print(line)

        # Asking which cell to access and which value to put into it.
        row = int(input('Please enter a row: '))
        column = int(input('Please enter a column: '))
        number = int(input('Please enter a number to be put in this row and column: '))

        # The if statement is true when the column chosen is not empty and already contains a non-zero element.
        if partialMagicSquare[row][column] != 0:
            print('This is an invalid entry as this cell already contains a number. Please select another cell.')

        # if the cell chosen is empty,the number input by the user is put in the cell if the number doesnt violate the partialMagicSquare property.
        else:
            partialMagicSquare[row][column] = number

            firstDiagonalSum = 0

            secondDiagonalSum = 0
            y = len(partialMagicSquare)

            # nested loop to access each cell in the partialMagicSquare
            for i in range(len(partialMagicSquare)):
                rowSum = 0
                columnSum = 0


                for j in range(len(partialMagicSquare)):
                    rowSum = rowSum + partialMagicSquare[i][j]
                    columnSum = columnSum + partialMagicSquare[j][i]


                if rowSum <= magicSum and columnSum <= magicSum:    # The program continues to run when this statement is true
                    pass


                else:
                    print('Invalid entry as it violates the magic square property. Please try again.')
                    partialMagicSquare[row][column] = 0
                    break

                firstDiagonalSum = firstDiagonalSum + partialMagicSquare[i][i]

                y = (y-1)         # decrementing the index to access the cells on the right diagonal

                secondDiagonalSum = secondDiagonalSum + partialMagicSquare[y][i]


            if firstDiagonalSum <= magicSum and secondDiagonalSum <= magicSum:      # The program continues to run when this statement is true
                pass

            else:
                print('Invalid entry as it violates the magic square property. Please try again.')
                partialMagicSquare[row][column] = 0



    else:
        cont = False           # if user inputs anything apart from Yes or No this else loop is executed(Program stops)
