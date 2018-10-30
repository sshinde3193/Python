# The program computes the determinant of a given square matrix
# Program accepts an N x N matrix as a comma separated file

import csv
import string
from permute import factorial_iterative
from permute import convert_B10_to_BBang
from permute import sum_BBang

def read_csv(filename):
    '''
    This function reads a csv file (which contains a N x N matrix in our case)
    :param: None
    :precondition: A file must exist either in csv or txt format
    :postcondition: The file is read
    :return: The contents of the file are returned
    :complexity: Best Case = Worst Case = O(1), since these are single individual statements therefore constant time complexity.
    '''

    read_file = open(filename, 'r')
    csv_r = csv.reader(read_file)
    return csv_r

def append_matrix():
    '''
    This function takes the read data (matrix) from the csv file and appends it into a list
    :param: None
    :precondition: The csv file must have been read
    :postcondition: The N x N matrix from the file is accepted and appended into a list
    :return: The N x N matrix is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the matrix
    '''

    matrix = []
    csv_matrix = read_csv(filename)
    for row in csv_matrix:
        matrix.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = int(matrix[i][j])
    return matrix

def check_sqmatrix():
    '''
    This function checks whether the file contained a square N x N matrix
    :param: None
    :precondition: The file must be read first
    :postcondition: We find out whether the file contained a square matrix or not
    :return: Returns True if a square matrix exists in the csv file or if it doesn't contain a square matrix it returns False
    :complexity: Best Case = Worst Case = O(n), where n is the length of the matrix
    '''

    matrix = append_matrix()
    row1_len = len(matrix[0])
    for i in range(1, len(matrix)):
        if row1_len != len(matrix[i]):
            return False
        elif row1_len != len(matrix):
            return False
    return True

def matrix_determinant(N):
    '''
    This function computes the determinant of a given square matrix using the permutation method
    :param: N i.e. the length of the matrix
    :precondition: The matrix should be a square matrix
    :postcondition: The determinant of the given square matrix is calculated using the permutation method
    :return: The determinant value is returned of the given matrix
    :complexity: Best case = Worst Case = O(n! * n^2), where n! is for iterating over all the permutations and O(n^2) for the extra loop and calling converting to BBang
    '''

    if check_sqmatrix() is False:
        return 'Error'
    else:
        matrix = append_matrix()
        N = len(matrix)
        factorial = factorial_iterative(N)
        perm_list = []
        determinant = 0
        for i in range(factorial):
            b_bang_numbers = convert_B10_to_BBang(N, i)
            permutation = convert_BBang_to_pstring(N, b_bang_numbers)
            total_sum = sum_BBang(b_bang_numbers)
            sgn_perm = perm_sign(total_sum)
            for number in permutation:
                perm_list.append(int(number))
            product = 1
            for k in range(len(matrix)):
                product *= matrix[perm_list[k] - 1][k]
            determinant += sgn_perm * product
        return determinant


def base_permutation(N):
    '''
    This function returns the base fully ordered permutation digits list (base_digits)
    :param: An integer N i.e also the size of the permutation in this case
    :precondition: None
    :postconditon: A fully ordered permutation is constructed i.e. the base digit list for any respective input N
    :return: Fully ordered permutation list for e.g N = 3, [1,2,3]
    :complexity: Best Case = Worst Case = O(n), where n is the size of the list
    '''

    basedigit_list = []
    base_digits = string.digits
    for i in range(1, N+1):
        basedigit_list.append(base_digits[i])
    return basedigit_list

def convert_BBang_to_pstring(N, BBang_list):
    '''
    This function pops the letters based on index and adds them to a string to create a permutation of letters
    :param: An integer N which is the size of string and the base-! digits list
    :precondition: None
    :postcondition: A new permutation string is produced from the base-! digits using the base string
    :return: Returns the permutation string from the base-! digits
    :complexity: Best Case = Worst Case = O(n), where n is the size of the list
    '''

    p_string = ''
    basestring_list = base_permutation(N)
    for i in range(len(BBang_list)):
        p_string += basestring_list.pop(BBang_list[i])
    return p_string


def perm_sign(perm):
    '''
    This function checks whether the total number of inversions of the permutation are even or odd and returns the sign depending on that
    :param: The total sum of the respective permutation
    :precondition: None
    :postconditon: None
    :return: returns +1 if it is even and -1 if odd
    :complexity: Best Case = Worst Case = O(1), constant time complexity
    '''

    if perm % 2 == 0:
        return +1
    else:
        return -1

def print_sqmatrix(file):
    '''
    This function writes the square matrix to the output file in the output format required if its a square matrix or else writes out Error
    :param: None
    :precondition: The matrix must be a square matrix
    :postcondition: The square matrix writes the matrix to the output file
    :return: None
    :complexitiy: Best Case = Worst Case = O(1), constant time complexity as these are singular statements
    '''

    if check_sqmatrix() is True:
        matrix = append_matrix()
        for row in matrix:
            file.write(''.join(str(row).strip('[]') + '\n'))
    else:
        file.write('Error')

def print_output_file():
    '''
    This function prints the output to a text file in a specific format
    :param: None
    :precondition: None
    :postcondition: The output is printed out to a text file with the length of the matrix, the matrix itself and its determinant value
    :return: None
    :complexity: Best Case = Worst Case = O(n), where n is the number of rows of the matrix
    '''

    matrix = append_matrix()
    N = len(matrix)
    file = open('Q3_Output.txt', 'w')
    file.write('N = ' + str(N) + '\n')
    file.write('Input Matrix:' + '\n')
    print_sqmatrix(file)
    file.write('\n' + 'Determinant = ' + str(matrix_determinant(N)))


if __name__ == '__main__':
    filename = input('Enter the filename: ')
    print_output_file()
