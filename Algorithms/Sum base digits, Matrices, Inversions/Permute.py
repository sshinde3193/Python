# Permute accepts integer N as argument
# For the given N, program should iterate over N! numbers

import string

def factorial_iterative(N):
    '''
    This function calculates the factorial for the given N iteratively.
    :param: An integer N whose factorial is calculated
    :precondition: The integer N should be >= 0
    :postcondition: The factorial value of N is calculated
    :return: The factorial value of the given N is returned
    :complexity: Best Case = Worst Case = O(n), where n is the number of steps
    '''

    result = 1
    for i in range(N):
        result *= (i+1)
    return result

def convert_B10_to_BBang(N, D):
    '''
    This function converts each perm number from its base 10 representation to its respective base-! representation
    :param: An integer N and an index D in base-10
    :precondition: The integer N inputted is > 0 and <= 10
    :postcondition: The numbers are converted from base 10 representation to their respective base-! representations
    :return: A list is returned with the corresponding base-! representations of the respective base-10 numbers
    :complexity: Best Case = Worst Case = O(n^2), where n is the number of steps
    '''

    BBang_list = []
    for i in range(1, N + 1):
        quotient = D // factorial_iterative(N-i)
        remainder = D % factorial_iterative(N-i)
        BBang_list.append(quotient)
        D = remainder
    return BBang_list

def full_order_perm(N):
    '''
    This function returns the base fully ordered permutation string
    :param: An integer N i.e also the size of the string in this case
    :precondition: None
    :postconditon: A fully ordered permutation is constructed i.e. the base string for any respective input N
    :return: Fully ordered permutation string for e.g N = 4, ['a','b','c','d']
    :complexity: Best Case = Worst Case = O(n), where n is the size of the list
    '''

    basestring_list = []
    alphabet_string = string.ascii_lowercase
    for i in range(N):
        basestring_list.append(alphabet_string[i])
    return basestring_list

def convert_BBang_to_pstring(N, BBang_list):
    '''
    This function pops the letters based on index and adds them to a string to create a permutation of letters
    :param: An integer N which is the size of string and the base-! digits list
    :precondition: None
    :postcondition: A new permutation string is produced from the base-! digits using the base string
    :return: Returns the permutation string from the base-! digits
    :complexity: Best Case = Worst Case = O(n^2), where n is the size of the list
    '''

    p_string = ''
    basestring_list = full_order_perm(N)
    for i in range(len(BBang_list)):
        p_string += basestring_list.pop(BBang_list[i])
    return p_string


def sum_BBang(BBang_list):
    '''
    This function calculates the sum of the base-! digits for a given permutation
    :param: The list of base-! digits
    :precondition: None
    :postcondition: The sum of the base-! digits is calculated for each respective permutation
    :return: The sum of the base-! digits is returned for the given permutation
    :complexity: Best Case = Worst Case = O(n), where n is the length of the list
    '''

    sum = 0
    for i in range(len(BBang_list)):
        sum += BBang_list[i]
    return sum

def max_sum(b_10_number):
    '''
    This function calculates the max sum which is required for us to set up the frequency list of length equal to the max sum for any given N
    :param: An integer N in base-10
    :precondition: None
    :postcondition: We get the maximum sum which we use to set up the frequency list of length equal to max sum
    :return: The maximum sum is returned
    :complexity: Best Case = Worst Case = O(n), where n is the number of steps
    '''

    m_sum = 0
    for i in range(b_10_number):
        m_sum += i
    return m_sum

def frequency_list(b_10_number):
    '''
    This function sets up the frequency list of the possible sum values with a length equal to the max sum for any given N
    :param: An integer N in base-10
    :precondition: The max sum must be calculated first
    :postcondition: We get a frequency list of size equal to the max sum
    :return: A frequency list is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the list
    '''

    freq_list = []
    length_list = max_sum(b_10_number)
    for i in range(length_list + 1):
        freq_list.append(0)
    return freq_list

def weighted_average(freq_list):
    '''
    This function calculates the weighted average of the sum of base-! digits over all permutations
    :param: frequency list which consists of the frequency of each sum
    :precondition: A frequency list must have been created
    :postcondition: We get the weighted average of the sum of base-! digits over all permutations
    :return: The weighted average of the sum of base-! digits over all permutations is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the frequency list
    '''

    sum_fx = 0
    total_weight = 0
    for i in range(len(freq_list)):
        sum_fx += (i * freq_list[i])
        total_weight += freq_list[i]
    weighted_avg = sum_fx / float(total_weight)
    return weighted_avg

def print_output_file():
    '''
    This function prints the output to a text file in a specific format
    :param: None
    :precondition: None
    :postcondition: The output is printed out to a text file with all permutations in lexographic order containing specific information
    :return: None
    :complexity: Best Case = Worst Case = O(n), where n is the number of permutations
    '''

    file = open('Q1_Output(a-c).txt', 'w')                                                          # opens file and writes to it
    b_10_number = int(input('Enter the base 10 number to be converted to base-!: '))
    file.write('INPUT TO THE SCRIPT: N = ' + str(b_10_number) + '\n')
    if 0 < b_10_number <= 10:
        factorial = factorial_iterative(b_10_number)                        # calculates factorial of number inputted by user
        file.write('TOTAL NUMBER OF PERMUTATIONS = ' + str(factorial) + '\n' + 'Base-10\t Base-!\t Sum\t Permutation')
        freq_list = frequency_list(b_10_number)
        for i in range(factorial):                                          # loops over all the possibilities of numbers
            b_bang_numbers = convert_B10_to_BBang(b_10_number, i)           # converts each base 10 number into base-!
            total_sum = sum_BBang(b_bang_numbers)
            freq_list[total_sum] += 1
            permutation = convert_BBang_to_pstring(b_10_number, b_bang_numbers)
            file.write('\n' + '(' + str(i) + ')' + '_10' + '\t' + '(' + ''.join(str(x) for x in b_bang_numbers) + ')_!' + '  ' + str(total_sum) + '\t' + '  ' + permutation + '\n')
        file.write('\n' + 'FREQUENCY' + '\t' + 'TABLE' + '\n' + '----------------------' + '\n' + '  ' 'SUM' + '\t' + '  ' + 'FREQ.')
        for j in range(len(freq_list)):
            file.write('\n' + '   ' + str(j) + '\t' + '   ' + str(freq_list[j]))
        file.write('\n' + 'Weighted average of sum = ' + str(weighted_average(freq_list)))


if __name__ == '__main__':
    print_output_file()
