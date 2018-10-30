import Task_2


class ArrayOperations:

    def __init__(self):
        '''
        Every time an object is created using the ArrayOperations class, an array is created of a fixed size of 100
        :param: None
        :precondition: the size must be fixed
        :postcondition: An array is created of size 100
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        self.size = 100
        self.array = [None] * self.size
        self.count = 0

    def __str__(self):
        '''
        This function returns the string representation of the list, each item of the string is printed on a new line
        :param: None
        :precondition: An array must already have been created with a size > 0
        :postcondition: A string representation of the list is printed with each item of the string printed on a new line
        :complexity: Best Case = Worst Case = O(n), where n is the length of the list
        '''

        output = ""
        for i in range(self.count):
            output += str(self.array[i])
            output += "\n"
        return output

    def __len__(self):
        '''
        This function returns the length of the array
        :param: None
        :precondition: None
        :postcondition: The length of the list is returned
        :oomplexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return self.count

    def __contains__(self, item):
        '''
        This function returns True or False depending whether the array contains the item the user is searching for, if found its True, else its False
        :param: item the user is searching for
        :precondition: An array must have already been created
        :postcondition: Returns True or False depending upon whether the item is found in the array
        :complexity: Best Case = O(1) , where the length of the array is 0
                     Worst Case = O(n), where n is the length of the array and n > 0
        '''

        result = False
        for i in range(self.count):
            if self.array[i] == item:
                result = True
        return result

    def __getitem__(self, index):
        '''
        This function returns the item in the array at the index entered by the user
        :param: index of the item entered by the user
        :precondition: None
        :postcondition: If the index entered is valid, the item is returned, or else the function throws an exception as the index may not exist for the size of the list
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        index -= 1
        if index < 0:
            raise IndexError                                             # handling for index < 0 and index > self.count
        elif index in range(self.count):
            return self.array[index]
        else:
            raise IndexError

    def __setitem__(self, index, item):
        '''
        This function sets the item value at the index stated by the user
        :param: index of where the item should be placed and the value of the item that should be placed
        :precondition: None
        :postcondition: The array is updated with a new item entered into the list at a particular index
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        index -= 1
        if index < 0:
            raise IndexError
        elif index in range(self.count):                                # handling for index < 0 and index > self.count
            self.array[index] = item
        else:
            raise IndexError

    def __eq__(self, other):
        '''
        This function checks whether the array is equivalent to another array, returns True or False depending upon that.
        :param: other comparison list
        :precondition: Another array to be compared with must exist
        :postcondition: It determines whether the list is equal to the other list
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        result = False
        if len(self) == len(other):
            for i in range(self.count):                                         # handling for the length of both lists
                if self.array[i] != other[i]:                                   # handling whether each item of both lists are identical, if not, result is false
                    result = False
                    break
                else:
                    result = True
            return result
        return result

    def is_full(self):
        '''
        This function checks whether the array is full
        :param: None
        :precondition: None
        :postcondition: Determines whether the array is full by returning either true or false depending upon the count compared to the length of the list
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return self.count >= len(self.array)

    def append(self, item):
        '''
        This function appends an item at the end of the list (the first None it finds, appends it at count as the index)
        :param: item to be put at the end of the list
        :precondition: A list must exist
        :postcondition: The list has a new value inputted into it at the count index, contains all original elements in same order and an additional element at end of array
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        self.array[self.count] = item
        self.count += 1
        if self.is_full():
            self.resize_list()                                              # if the list is full, the list is re-sized

    def insert(self, index, item):
        '''
        This function inserts the item entered at the index position in the array inputted by the user and shifts the remaining list to the right
        :param: item value to be inserted into the array and the index at which the item should be placed in the array
        :precondition: Space in the array must exist before the particular index value inputted
        :postcondition: A new list is returned with the inputted value in the list
        :complexity: Best Case = O(n), when list has at least one item
                     Worst Case = O(1), when list is empty, index error will be raised
        '''

        index -= 1
        has_space_left = not self.is_full()
        if has_space_left:
            if index < 0 or index > self.count:
                raise IndexError
            else:
                for i in range(self.count - 1, index - 1, -1):
                    self.array[i + 1] = self.array[i]                        # shifting the list to make space for the item to be inserted and then inserting the item in the list
                self.array[index] = item
                self.count += 1
        else:
            self.resize_list()
            if index < 0 or index > self.count:
                raise IndexError
            else:
                for i in range(self.count - 1, index - 1, -1):
                    self.array[i + 1] = self.array[i]                       # shifting the list to make space for the item to be inserted and then inserting the item in the list
                self.array[index] = item
                self.count += 1

    def remove(self, item):
        '''
        This function uses linear search and the first item it finds that is searched for, it deletes that item from the list
        :param: item the user wants to delete from the list
        :precondition: None
        :postcondition: The first instance of the item searched for is deleted from the list and the list adjusts the space left by the deletion itself
        :complexity: Best Case = O(n), where n is the length of the list, when the item is found
                     Worst Case = O(n), where n is the length of the list, when the item is not found
        '''

        result = False
        while result == False:
            for i in range(self.count):
                if item == self.array[i]:                           # Linear search and then calling the delete function
                    self.delete(i)
                    result = True
                    break
                else:
                    result = False
            if result == False:                                     # if item not found raises ValueError
                raise ValueError

    def delete(self, index):
        '''
        This function deletes the item at index from the list and moves all the rest of the items towards the start of the list
        :param: index of the item which should be deleted from the list
        :precondition: There must be an existing item at the index inputted to be deleted from the list
        :postcondition: The list is returned with all the original elements of the list except the deleted element
        :complexity: Best Case = O(n), where n is the length of the list, when the item to be deleted is found
                     Worst Case = O(1), when the index is not valid
        '''

        index -= 1
        valid_index = index >= 0 and index < self.count
        if valid_index:
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.count -= 1
        else:
            raise IndexError                                    # if index not valid, raises ValueError


    def resize_list(self):
        '''
        This function resizes the list by 10 times every time the list becomes full.
        :param: None
        :precondition: The size of the list must be full
        :postcondition: The list has increased by 10 times in size while retaining the original contents of the original list
        :complexity: Best Case = Worst Case = O(n), linear time complexity.
        '''

        tmp = [None] * (len(self.array) * 10)                               # resize tmp list
        for i in range(self.count):
            tmp[i] = self.array[i]                                          # copy original items of original list into tmp
        self.array = tmp                                                    # make original list equal to tmp
        return self.array



if __name__ == '__main__':

    array = ArrayOperations()
