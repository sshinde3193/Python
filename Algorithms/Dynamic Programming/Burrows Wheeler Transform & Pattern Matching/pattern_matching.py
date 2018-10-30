from invBWT import read_bwt
from invBWT import rank_table
from quicksort1 import quick_sort

def read_file(patt_filename):
    '''
    This function reads the file containing all the patterns to be matched and stores them in a list
    :param: Any supplied text file containing the patterns
    :precondition: The file must contain the pattern which need to be looked for
    :postcondition: The list is created with the patterns that need to be searched for
    :return: The pattern list containing the patterns to be searched for in the text
    :complexity: Best Case = Worst Case = O(n), where n is the number of patterns
    '''

    file = open(patt_filename, 'r')
    pattern = file.readlines()
    pattern_list = []
    for i in range(len(pattern)):
        pattern_list.append(pattern[i].strip('\n'))
    return pattern_list

def no_occurence_freq_tb(bwt_filename):
    '''
    This function creates the 2D number of occurence table for the BWT using ASCII values and also keeps count of freq in a freq table
    :param: Any supplied text file containing the bwt
    :precondition: The bwt must have already been created
    :postcondition: The 2D number of occurence table and freq table are constructed
    :return: The number of occurence table and frequency table are returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the list
    '''
    # storing values inclusive of pointer value

    bwt_list = read_bwt(bwt_filename)
    freq_tb = dict()
    occ_tb = [[0 for x in range(128)] for y in range(1, len(bwt_list))]
    for i in range(1, len(bwt_list)):
        if bwt_list[i] not in freq_tb:
            freq_tb[bwt_list[i]] = 1
        else:
            freq_tb[bwt_list[i]] += 1
        occ_tb[i-1][ord(bwt_list[i])] += 1
        if i > 1:
            for j in range(128):
                occ_tb[i-1][j] += occ_tb[i-2][j]
    return occ_tb, freq_tb

def read_SA():
    file_r = open('suffarray.txt', 'r')
    suff_array = file_r.read()
    suff_array = suff_array.split(' ')
    return suff_array

def search_patterns(bwt_filename):
    '''
    This function searches for the given patterns in the text and returns the no of occurences and the positions where that pattern appears in the original text
    :param: Any supplied text file with the bwt
    :precondition: The bwt must exist and the occurence table and rank table should have already been created
    :postcondition: The number of occurrences of the pattern and the position of the pattern where it occurs in the text is found
    :return: None
    :complexity: Best Case = Worst Case = O(n^2), where n is the len of the pat list
    '''

    file = open('outputTask3.txt', 'w')
    bwt_list = read_bwt(bwt_filename)
    pattern_list = read_file(patt_filename)
    new_occ_tb, freq_tb = no_occurence_freq_tb(bwt_filename)
    rank_tb, old_occurences = rank_table(bwt_filename)
    suff_array = read_SA()
    for i in range(len(pattern_list)):
        sp = 1
        ep = len(bwt_list) - 1
        j = len(pattern_list[i]) - 1
        while j >= 0:
            sp = rank_tb[pattern_list[i][j]] + new_occ_tb[sp-1][ord(pattern_list[i][j])] - 1
            ep = rank_tb[pattern_list[i][j]] + new_occ_tb[ep-1][ord(pattern_list[i][j])] - 1
            j -= 1
        patt_appears_count = (ep - sp)
        file.write('Pattern ' + pattern_list[i] + ' appears ' + str(patt_appears_count) + ' times.' + '\n')
        if patt_appears_count != 0:
            file.write('Its positions in the original string in the SORTED ORDER: ' + '\n')
        temp = [None]
        for k in range(sp, ep):
            temp.append(int(suff_array[k]))
        quick_sort(temp)
        for pos in range(len(temp)):
            if temp[pos] != None:
                file.write(str(temp[pos]) + '\n')
        file.write('\n')

if __name__ == '__main__':
    bwt_filename = 'bwt1000001.txt'
    org_string_filename = 'originalstring.txt'
    patt_filename = 'shortpatterns.txt'
