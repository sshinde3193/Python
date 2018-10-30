from quicksort import quick_sort

class QuadraticProbeHashTable:

    def __init__(self, size):

        '''
        When an object is created using the QuadraticProbeHashTable, a table with linear probing of a default size is created.
        :param: Size of the table (size is a prime number)
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity, since there are single statements being executed.
        '''

        self.array = [None] * size
        self.table_size = size
        self.count = 0

    def hash(self, key):
        '''
        This function is the universal hash function which calculates the hash value for the given key.
        :param: The keys in the hash table
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(n), where n is the length of hash table
        '''

        value = 0
        a = 31415
        b = 27183
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.table_size
            a = a * b % (self.table_size - 1)
        return value

    def __setitem__(self, key, value):
        '''
        This function puts the value corresponding to the key at the position which is empty in the Hash Table or
        updates a value if there is something in the position with the same key or finds a new empty spot if there is
        already something there with a different key. (Uses linear search)
        :param: Key and its corresponding value
        :precondition: None
        :postcondition: None
        :complexity: Best Case O(1), constant time complexity, if the code does not enter the for loop and raises exception
                     Worst Case O(n), linear time complexity, where n is the size of the hash table.
        '''

        position = self.hash(key)
        fixed_position = position
        copyPos = position
        if self.count == self.table_size:
            self.rehash(size)
        for i in range(self.table_size):
            if self.array[position] is None:                    # if the slot is empty in the table it sets the value at that position
                self.array[position] = (key, value)
                self.count += 1
                return
            elif self.array[position][0] == key:                # if the same key is found it updates the value at that position
                self.array[position] = (key, value)
                return
            else:
                position = (fixed_position + ((i + 1) ** 2)) % self.table_size     # if key is not found, look for the next position
                if copyPos == position:
                    raise Exception('High load factor')

    def __getitem__(self, key):
        '''
        This function returns the value corresponding to the key at the position in the Hash Table. The function raises
        a KeyError if the key does not exist in the Hash Table
        :param: The key which may or may not exist in the Hash Table
        :precondition: None
        :postcondition: The value is returned corresponding to the key in the hash table or a KeyError if key does not exist
        :complexity: Best Case = Worst Case = O(n), where n is the size of the table
        '''

        position = self.hash(key)
        fixed_position = position
        for i in range(self.table_size):
            if self.array[position] is None:                            # at that key position there is an empty slot
                break
            elif self.array[position][0] == key:                        # if the same key is found we return the value at that key
                return self.array[position][1]
            else:
                position = (fixed_position + ((i+1) ** 2)) % self.table_size    # if the key is not found, we look for the next position
        raise KeyError(key)                                               # if the for loop exits without returning means key does
                                                                          # not exist the hash table

    def __contains__(self, key):
        '''
        This function returns True if key is in the table and False otherwise.
        :param: The key which may or may not exist in the table
        :precondition: A hash table must already exist
        :postcondition: Returns true or false depending on whether the key exists in the table or not
        :complexity: Best Case = Worst Case = O(n), where n is the size of the hash table
        '''

        position = self.hash(key)
        fixed_position = position
        for i in range(self.table_size):
            if self.array[position] is None:                        # at that key position there is an empty slot, hence false since key does not exist there
                return False
            elif self.array[position][0] == key:                    # if the same key is found we return true as the key is found
                return True
            else:
                position = (fixed_position + ((i+1) ** 2)) % self.table_size         # if the key is not found, we look for the next position in the hash table
        return False

    def delete(self, key):
        '''
        This function takes key as the input and then deletes the entry corresponding to the key, raises a keyerror if key not in the table
        :param: key
        :precondition: None
        :postcondition: None
        :complexity: Best Case O(1) and Worst Case O(n)
        '''

        if key not in self:
            raise KeyError
        position = self.hash(key)
        fixed_position = position
        for i in range(self.table_size):
            if self.array[position][0] == key:
                self.array[position] = (None, None)
                return
            else:
                position = (fixed_position + ((i + 1) ** 2)) % self.table_size

    def rehash(self, size):
        '''
        This function changes the size of the table and reinserts all the key value pairs. It raises a valuerror if size < 1
        :param: size
        :precondition: None
        :postcondition: None
        :complexity: Best Case O(1) and Worst Case O(n)
        '''

        if size < 1:
            raise ValueError
        resize_table = QuadraticProbeHashTable(size)
        for i in range(self.table_size):
            if self.array[i] is None or self.array[i] == (None, None):
                continue
            else:
                resize_table[self.array[i][0]] = self.array[i][1]
        self.array = resize_table.array
        self.size = resize_table.size

def read_file(L):
    '''
    This function reads the file splitwords, adds the distinct words in the file into a Quadratic Probe Hash Table and appends them into a list as well
    :param: We pass the Hashtable through as an argument
    :precondition: The file splitwords.txt must already exist
    :postcondition: The HashTable is filled up with the respective keys(words) and their initial frequency values of 0 as a counter.
    :return: The word list and the hashtable is returned
    :complexity: Best Case = Worst Case = O(n), where n is the length of the contents (no of rows in the txt file)
    '''

    word_list = []
    file = open('splitwords.txt', 'r')
    contents = file.readlines()
    for word in range(len(contents)):
        word_list.append(contents[word].rstrip('\n'))
        L[contents[word].rstrip('\n')] = 0
    return word_list, L

def calc_freq(L):
    '''
    This function sorts the word list and increments the frequency of the words in the hashtable, creates a final unique word list and sorts it
    :param: We pass the hashtable through as an argument
    :precondition: The word_list and hashtable must exist with the respective words and values
    :postcondition: The hashtable now contains the words with their respective frequencies and the word_list is also sorted, and a new unique sorted list is created
    :return: Sorted word list and the hashtable
    :complexity: Best Case = Worst Case = O(n), where n is the length of the list
    '''

    word_list, L = read_file(L)
    final_word_list = []
    for word in word_list:
        L[word] += 1
        if word not in final_word_list:
            final_word_list.append(word)
    quick_sort(final_word_list)
    return final_word_list, L

def write_file(L):
    '''
    This function writes the words in sorted order with their respective frequencies to an output text file
    :param: The hash table
    :precondition: None
    :postcondition: The output is written to a text file
    :return: None
    :complexity: Best Case = Worst Case = O(n), where n is the length of the final word list
    '''

    file = open('frequencies.txt', 'w')
    final_word_list, L = calc_freq(L)
    for word in final_word_list:
        file.write(word + '\t' + str(L[word]) + '\n')
    file.close()

if __name__ == '__main__':
    size = 402221
    h = QuadraticProbeHashTable(size)
    write_file(h)
