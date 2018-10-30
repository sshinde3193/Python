from quicksort_prefix_doub import quick_sort

def read_org_string_file(org_string_filename):
    '''
    This function reads in the original string from the file and appends into a list index by index
    :param: Any supplied text file containing the string
    :precondition: The supplied text file must contain the original string
    :postcondition: The original string is read from the file into a list
    :return: The list containing the original string is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the original string
    '''

    file = open(org_string_filename, 'r')
    org_string = file.read().strip('\n')
    org_list = [None]
    for i in range(len(org_string)):
        org_list.append(org_string[i])
    return org_list

def SA():
    '''
    This function creates the index suffix array
    :param: None
    :precondition: The supplied text file containing the original string must have already been read
    :postcondition: A list containing the suffix indexes is created
    :return: The index suffix array is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the orignal string
    '''
    sa = [None]
    org_list = read_org_string_file(org_string_filename)
    for i in range(1, len(org_list)):
        sa.append(i)
    return sa

def rank_table(org_string_filename):
    '''
    This function creates the rank table with the suffix pointers pointing towards each respective rank
    :param: Any supplied text file containing the original string
    :precondition: The index suffix array must have been created and original string must have been read
    :postcondition: The rank table has been initialised for the original string
    :return: The rank table is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the list
    '''

    org_list = read_org_string_file(org_string_filename)
    sa = SA()
    rank_tb = [None for j in sa]
    for i in range(1, len(sa)):
        rank_tb[i] =  ord(org_list[i])
    return rank_tb

def prefix_doubling(org_string_filename):
    '''
    This function does the prefix doubling and keeps sorting and updating the rank table
    :param: Any supplied text file containing the original string
    :precondition: The index suffix array and rank table must have been already created
    :postcondition: The sorted suffix array is constructed
    :return: The sorted suffix array is returned after using the prefix doubling method
    :complexity: 
    '''

    sa = SA()
    rank_tb = rank_table(org_string_filename)
    for k in range(1, len(rank_tb)):
        quick_sort(sa, lambda i, j: suffix_compare(rank_tb, k//2, i, j))
        temp = [0] * len(rank_tb)
        for i in range(1, len(rank_tb) - 1):
            temp[sa[i+1]] = temp[sa[i]] + suffix_compare(rank_tb, k//2, sa[i], sa[i+1])
        rank_tb = temp
        k *= 2
    return sa

def suffix_compare(rank_tb, k, i, j):
    '''
    :param k: half the length of the sorted suffix
    :param i: starting point of the suffix being compared 
    :param j: ending point of the suffix being compared
    :precondition: The rank table must have already been constructed
    :postcondition: The rank values are compared
    :return: Boolean values are returned after comparison
    :complexity: Best Case = Worst Case = O(1), constant time complexity since there are single statements.
    '''

    N = len(rank_tb) - 1
    if rank_tb[i] != rank_tb[j]:
        return rank_tb[i] < rank_tb[j]
    elif i + k <= N and j + k <= N:
        return rank_tb[i + k] < rank_tb[j + k]
    else:
        return j < i

def generate_bwt(filename):
    '''
    This function generates the BWT using the suffix array previously computed by using Manber-Myers' Algorithm
    :param: Any supplied text file
    :precondition: The suffix array must have already been computed
    :postcondition: The BWT for the given string is computed using the suffix array indexing & written to an output file
    :return: The BWT (last column) of the given string is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the given string, since suffix arrays can be
                 computed in linear time, therefore, the BWT can also be computed in linear time
    '''

    original_string = read_org_string_file(filename)
    suff_array = prefix_doubling(org_string_filename)
    bwt = [None] * len(suff_array)
    for i in range(1, len(suff_array)):
        if suff_array[i] == 1:
            bwt[i] = '$'
        else:
            bwt[i] = original_string[suff_array[i]-1]
    return ''.join(bwt[1:])

def bwt_write_file(filename):
    '''
    This function writes the bwt generated to an output text file called outputbwt.txt
    :param: Any supplied text file
    :precondition: The bwt must already have been computed to be written to the output text file
    :postcondition: The bwt is written to the output text file
    :return: None
    :complexity: Best Case = Worst Case = O(1), Constant time complexity, since single code statements are being executed
    '''

    bwt = generate_bwt(filename)
    file = open('outputbwt.txt', 'w')
    file.write(bwt)

if __name__ == '__main__':
    org_string_filename = input('Enter the filename: ')
    bwt_write_file(org_string_filename)
