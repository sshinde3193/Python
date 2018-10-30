def createList():
    '''
    This function reads in the size of the temperature list, allocates the required amount of space and reads in each value into the temperature list.
    :param: None
    :precondition: None
    :postcondition: Creates a list
    :complexity: Best Case O(n), Worst Case O(1)
    '''

    size = int(input('Enter the size of the temperature list: '))                # takes the size of the list from user
    temp_list = [0] * size
    i = 0
    while i < len(temp_list):
        temp_list[i] = int(input())                         # takes the input of the elements of the list at each index
        i += 1
    return temp_list

def bubbleSort(temp_list):
    '''
    This function sorts the temperatures in the list in increasing order and then returns the temperature list.
    :param: temp_list
    :precondition: The temp_list must not be empty.
    :postcondition: The list returned is sorted.
    :complexity: Best Case O(n), Worst Case O(n^2)
    '''

    i = 0
    while i < len(temp_list) - 1:
        j = i + 1
        while j < len(temp_list):
            if temp_list[i] > temp_list[j]:                     # Swapping the elements if the condition is true
                tmp = temp_list[i]
                temp_list[i] = temp_list[j]
                temp_list[j] = tmp
            j += 1
        i += 1
    return temp_list


def binarySearch(temp_list, target, startindex, endindex):
    '''
    This function implements binary search recursively to find the target value in the temperature list.
    :param: Temperature list, target value, startindex and endindex inputted by the user
    :return: True or False depending upon whether the target was found or not in the list.
    :precondition: The list must be sorted in ascending order
    :postcondition: None.
    :complexity: Best Case O(1), Worst Case O(n), where n is the length of the list
    '''


    if startindex == endindex:                                      # Base case, if the startindex equals endindex it will return False as the list would be empty
        return False
    mid = (startindex + endindex) // 2                              # Used to calculate the position of the middle element
    if temp_list[mid] == target:                                    # if the middle value equals the target value then it returns true
        return True
    elif temp_list[mid] > target:                                   # if the middle value in the temperature list is greater than the target value then we search the left half of the list
        return binarySearch(temp_list, target, startindex, mid)     # This is done by calling the binarySearch function with the parameter from start to the mid value
                                                                    # which is now the high, basically high = mid - 1  (i.e. the left half of the list)
    else:
        return binarySearch(temp_list, target, mid + 1, endindex)   # else the middle value in the temperature list is less than the target value then we search the right half of the list
                                                                    # This is done by calling the binarySearch function with the parameter from low to the end value
                                                                    # however now the low value is basically low = mid + 1  (i.e. the right half of the list)

temp_list = createList()
bubbleSort(temp_list)
target = int(input('Enter the target value to find in the temperature list: '))

if binarySearch(temp_list, target, 0, len(temp_list)):
    print('Temperature found')
else:
    print('Temperature not found')
