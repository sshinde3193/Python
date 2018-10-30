class Node:

    def __init__(self, item, link = None):
        '''
        This function creates a node and a link
        :param: item and link
        :precondition: None
        :postcondition: None
        :oomplexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        self.item = item
        self.next = link

    def __str__(self):
        '''
        This function returns the item in string format
        :param: item and link
        :precondition: None
        :postcondition: None
        :oomplexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return str(self.item)

class LinkedList:

    def __init__(self):
        '''
        This function creates the linked list by creating the head which acts as a pointer for the linked list and count at start is 0 as list is empty
        :param: None
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        self.head = None
        self.count = 0

    def is_empty(self):
        '''
        This function returns the linked list if it is empty i.e. when the count is 0
        :param: None
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return self.count == 0

    def is_full(self):
        '''
        This function tells us that the linked list can never be full, hence if he checks if the linked list is full it will always return false.
        :param: None
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return False

    def reset(self):
        '''
        This function resets the link list to empty as it was at the start when it was created.
        :param: None
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        self.__init__()

    def __len__(self):
        '''
        This function returns number of items in the list i.e. the count of the linked list.
        :param: None
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return self.count

    def __get_node__(self, index):
        '''
        This function gets the node of the next item till the end of the list
        :param: index
        :precondition: None
        :postcondition: None
        :complexity: Best Case = O(1), Worst Case = O(n)
        '''

        node = self.head
        for i in range(index):
            node = node.next
        return node

    def insert(self, index, item):
        '''
        This function is used to insert item into the list
        :param: Index and item to insert
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(n)
        '''

        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)
        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self.__get_node__(index - 1)
            node.next = Node(item, node.next)
        self.count += 1

    def __getitem__(self, index):
        '''
        This function returns the item at the head
        :param: index
        :precondition: None
        :postcondition: None
        :complexity: Best Case = O(1), Worst Case = O(n)
        '''
        current_node = self.head
        while index > 0:
            current_node = current_node.next
            index -= 1
        return current_node.item

    def __setitem__(self, index, value):
        '''
        This function sets the item at the head
        :param: index and value to set
        :precondition: None
        :postcondition: None
        :complexity: Best Case = O(1), Worst Case = O(n)
        '''

        current_node = self.head
        while index > 0:
            current_node = current_node.next
            index -= 1
        current_node.item = value

class SeperateChainingHashTable:

    def __init__(self, size, b):

        '''
        When an object is created using the SeperateChainingHashTable, a table with linear probing of a default size is created.
        :param: Size of the table (size is a prime number)
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity, since there are single statements being executed.
        '''

        self.array = [None] * size
        self.table_size = size
        self.count = 0
        self.b = b
        self.collision_counter = 0

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
        b = self.b
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.table_size
            a = a * b % (self.table_size - 1)
        return value

    def __setitem__(self, key, value):
        '''
        This function creates a linkedlist at the position if the position is empty in the Hash Table or
        updates a value if there is something in the position with the same key or finds a new empty spot if there is
        already something there with a different key.
        :param: Key and its corresponding value
        :precondition: None
        :postcondition: None
        :complexity: Best Case O(1), constant time complexity
                     Worst Case O(n), linear time complexity
        '''

        position = self.hash(key)
        if self.array[position] is None:                                                # if the slot is empty in the table it sets the value at that position
            self.array[position] = LinkedList()                                             # create a linkedlist at the empty position
            self.array[position].insert(self.array[position].count, (key, value))                # once linkedlist is created, you insert item into the list
            self.count += 1
            return
        elif self.array[position][0][0] == key:                                         # if the same key is found it updates the value at that position
            self.array[position][0] = (key, value)
            return
        else:
            self.array[position].insert(self.array[position].count, (key,value))
            self.collision_counter += 1
            return

    def __getitem__(self, key):
        '''
        This function returns the value corresponding to the key at the position in the Hash Table. The function raises
        a KeyError if the key does not exist in the Hash Table
        :param: The key which may or may not exist in the Hash Table
        :precondition: None
        :postcondition: The value is returned corresponding to the key in the hash table or a KeyError if key does not exist
        :complexity: Best Case = Worst Case = O(n)
        '''

        position = self.hash(key)
        if self.array[position] is None:               # if the linkedlist is empty, raise keyError as key is not found
            raise KeyError
        current = self.array[position].head
        while current.item != None:
            if current.item[0] == key:
                return current.item[1]
            else:
                current = current.next
        raise KeyError                                  # if the  is found we return the value at that key
                                                            # if the key is not found, we look for the next position                                                       # if the for loop exits without returning means key does
                                                                                    #  not exist the hash table

    def __contains__(self, key):
        '''
        This function returns True if key is in the table and False otherwise.
        :param: The key which may or may not exist in the table
        :precondition: A hash table must already exist
        :postcondition: Returns true or false depending on whether the key exists in the table or not
        :complexity: Best Case = Worst Case = O(n), where n is the size of the hash table
        '''

        position = self.hash(key)
        if self.array[position] is None:                    # if the linkedlist is empty, raise keyError as key is not found
            return False
        current = self.array[position].head
        while current.item != None:
            if current.item[0] == key:
                return True                                   # if the same key is found we return true as the key is found
            else:
                current = current.next                        # if the key is not found, we look for the next position in the hash table
        return False

    def no_collisions(self):
        '''
        This function returns the number of collisions
        :param: None
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return self.collision_counter


def read_file(filename,L):

    '''
    This function takes a filename as an input by the user and reads the contents of the file into a hash table, storing each line as a single item in the hash table
    :param: filename inputted by the user
    :precondition: A file must exist from which the contents of the file can be read
    :postcondition: A Hash table is filled with each line in the file stored as a single item in the hash table
    :complexity: Best Case = Worst Case = O(n), where n is the length of the contents in the file, even if the contents are empty or filled the loop will run n times
    '''

    infile = open(filename, 'r')
    contents = infile.readlines()
    for i in range(len(contents)):
        L[contents[i].rstrip('\n')] = contents[i].rstrip('\n')
    infile.close()

if __name__ == '__main__':

    filename = input('Enter the filename: ')

    b_list = [1, 27183, 250726]
    table_size = [250727, 402221, 1000081]
    for b in b_list:
        for size in table_size:
            if b == 250726 and size == 250727:
                continue
            h = SeperateChainingHashTable(size, b)
            import timeit
            start = timeit.default_timer()
            read_file(filename, h)
            time_taken = (timeit.default_timer() - start)
            print(time_taken)
            print(h.no_collisions())
