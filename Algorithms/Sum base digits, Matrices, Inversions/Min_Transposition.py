def convert_perm(perm1, perm2):
    '''
    This function takes any two permutations of a finite set of distinct letters and returns as an answer the smallest no of transpositions required to convert
    from one perm to another.
    :param: Two permutation strings which can both be converted to each other or vice versa
    :precondition:
    :postconditon: We get the smallest no of (adjacent) transpositions required to convert from one perm to the other or vice versa
    :return: The smallest number of (adjacent) transpositions required to convert from one perm to the other or vice versa are returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the base_string list
    '''

    basestring_list = []
    s_no_of_transpositions = 0
    for letter in perm1:
        basestring_list.append(letter)
    for letter in perm2:
        for i in range(len(basestring_list)):
            if letter == basestring_list[i]:
                s_no_of_transpositions += i
                basestring_list.pop(i)
                break
    return s_no_of_transpositions


if __name__ == '__main__':
    perm1 = input('Enter permutation string 1: ')
    perm2 = input('Enter permutation string 2: ')
    file = open('Q2_Output.txt', 'w')
    file.write('Input Permutation 1 = ' + perm1 + '\n' + 'Input Permutation 2 = ' + perm2 + '\n' + 'Output (smallest number of inversion) = ' + str(convert_perm(perm1,perm2)))
