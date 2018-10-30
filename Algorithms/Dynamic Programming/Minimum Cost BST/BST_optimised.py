def read_file():
    '''
    This function reads the frequency text file and returns the frequency list containing the frequency of all the keys
    :param: None
    :precondition: The frequencies.txt file must already exist
    :postcondition: We get the data which is in the file
    :return: The data of the file is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the list
    '''

    word_list = [None]
    freq_list = [None]
    file = open('frequencies.txt', 'r')
    contents = file.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i].strip('\n')
        pair = contents[i].split('\t')
        word_list.append(pair[0])
        freq_list.append(int(pair[1]))
    return freq_list, word_list

def sum_freq():
    freq_list, word_list = read_file()
    sum = 0
    for i in range(1, len(freq_list)):
        sum += freq_list[i]
    return sum

def probability_sum_table():
    freq_list, word_list = read_file()
    total_freq = sum_freq()
    prob_table = [[0 for x in range(len(freq_list))] for y in range(len(freq_list))]
    counter = 0
    while counter < len(prob_table):
        i = 0
        j = counter
        while i < len(prob_table) and j < len(prob_table):
            if i == j-1:
                prob_table[i][j] = freq_list[j] / float(total_freq)
            else:
                prob_table[i][j] = prob_table[i][j-1] + prob_table[j-1][j]
            i += 1
            j += 1
        counter += 1
    return prob_table

def min_cost_table():
    freq_list, word_list = read_file()
    prob_table = probability_sum_table()
    cost_table = [[0 for x in range(len(freq_list))] for y in range(len(freq_list))]
    root_table = [[None for x in range(len(freq_list))] for y in range(len(freq_list))]
    counter = 0
    while counter < len(cost_table):
        i = 0
        j = counter
        while i < len(cost_table) and j < len(cost_table):
            if i < j:
                minValue = None
                for r in range(i+1, j+1):
                    comb = cost_table[i][r-1] + cost_table[r][j]
                    if minValue == None:
                        minValue = comb
                    if minValue > comb:
                        minValue = comb
                root_table[i][j] = minValue
                cost_table[i][j] = prob_table[i][j] + minValue
            i += 1
            j += 1
        counter += 1
    return cost_table, root_table

#def level_ki(ki_list, i, j):
    #cost_table, root_table = min_cost_table()
    #if i == j:
        #return


def write_file():
    '''
    This function writes the output to the file in a specific format
    :param: None
    :precondition: None
    :postcondition: The required output is written to the text file
    :complexity: Best Case = Worst case = O(n), where n is the size of the list
    '''

    freq_list, word_list = read_file()
    file = open('mincostbst.txt', 'w')
    for i in range(1, len(word_list)):
        file.write(word_list[i] + '\t' + str(freq_list[i]) + '\n')

if __name__ == '__main__':
    write_file()
