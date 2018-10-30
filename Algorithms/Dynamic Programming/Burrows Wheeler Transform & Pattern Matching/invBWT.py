def read_bwt(filename):
    '''
    This function reads one line BWT string from the input text file provided by the user
    :param: Any supplied text file containing the BWT string
    :precondition: The text file must be provided and must contain the BWT string
    :postcondition: The file has been read and the one line BWT string is stored in a variable
    :return: The one line BWT string is returned in the form of a variable
    :complexity: Best Case = Worst Case = O(n), where n is the length of bwt string
    '''

    file = open(filename, 'r')
    bwt_string = file.read().strip('\n')
    bwt_list = [None]
    for i in range(len(bwt_string)):
        bwt_list.append(bwt_string[i])
    return bwt_list

def freq__occurence_table(filename):
    '''
    This function creates the frequency of each character table and a number of occurence table of that 
    character at that position which occurred earlier in the string.
    :param: Any supplied text file containing the BWT string
    :precondition: The text file must be provided and must contain the BWT string
    :postcondition: Two tables are constructed, one containing the freq of each character in the string and the other
                    containing number of occurence of that character at that position occurred earlier in the string
    :return: Number of occurences table and Frequency table of each character
    :complexity: Best Case = Worst Case = O(n), where n is the length of bwt string
    '''

    bwt_list = read_bwt(filename)
    freq_tb = dict()
    no_of_occurence_tb = [0] * (len(bwt_list) - 1)
    for i in range(1, len(bwt_list)):
        if bwt_list[i] not in freq_tb:
            freq_tb[bwt_list[i]] = 1
        else:
            freq_tb[bwt_list[i]] += 1
            no_of_occurence_tb[i-1] += freq_tb[bwt_list[i]] - 1
    return no_of_occurence_tb, freq_tb

def rank_table(filename):
    '''
    This function creates the rank table using the prefix sums of the counts in the frequency table
    :param: Any supplied text file containing the BWT string
    :precondition: The frequency table must have already been constructed
    :postcondition: The rank table is created containing the ranks of each distinct character
    :return: The rank table and number of occurence table is returned
    :complexity: Best case = Worst Case = O(n), where n is the length of the frequency table
    '''

    no_of_occurence_tb, freq_tb = freq__occurence_table(filename)
    freq_tb = sorted(freq_tb.items())
    rank_tb = dict()
    rank_tb[freq_tb[0][0]] = 1
    cf = [1]
    for i in range(1, len(freq_tb)):
        cf_val = cf[i - 1] + freq_tb[i][1]
        cf.append(cf_val)
        rank_tb[freq_tb[i][0]] = (cf_val - freq_tb[i][1]) + 1
    return rank_tb, no_of_occurence_tb

def invert_bwt(filename):
    '''
    This function uses the rank table and the no of occurence table to invert the BWT string to compute the original string and computes sa as well
    :param: Any supplied text file containing the BWT string
    :precondition: The rank table and the no of occurence table must already be constructed
    :postcondition: The original string is recovered
    :return: The original string is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the bwt string
    '''

    bwt_list = read_bwt(filename)
    rank_tb, no_of_occurence_tb = rank_table(filename)
    original_string_list = []
    original_string_temp = ['$', bwt_list[1]]
    length = len(bwt_list) - 1
    sa = [0] * len(bwt_list)
    sa[0] = None
    sa[1] = length
    j = 1
    while bwt_list[j] != '$':
        pos = rank_tb[bwt_list[j]] + no_of_occurence_tb[j-1]
        original_string_temp.append(bwt_list[pos])
        j = pos
        length -= 1
        sa[j] = length
    for i in range(-1, -len(original_string_temp)-1, -1):
        original_string_list.append(original_string_temp[i])
    original_string = ''.join(original_string_list[1:])
    return original_string, sa

def write_sa(filename):
    original_string, sa = invert_bwt(filename)
    for i in range(1, len(sa)):
        sa[i] = str(sa[i])
    sa_r = ' '.join(sa[1:])
    file = open('suffarray.txt', 'w')
    file.write(sa_r)

def write_file(filename):
    '''
    This function writes the original string recovered to an output text file called originalstring.txt
    :param: Any supplied text file
    :precondition: The original string must already have been computed to be written to the output text file
    :postcondition: The original string is written to the output text file
    :return: None
    :complexity: Best Case = Worst Case = O(1), Constant time complexity, since single code statements are being executed
    '''

    original_string, sa = invert_bwt(filename)
    file = open('originalstring.txt', 'w')
    file.write(original_string)

if __name__ == '__main__':
    filename = input('Enter the filename: ')
    invert_bwt(filename)
    write_file(filename)
    write_sa(filename)
