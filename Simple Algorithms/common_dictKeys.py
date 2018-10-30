def common_keys(dict1, dict2):
    '''
    This function finds all the common keys in the two dictionaries and appends them into a list
    :param: Dictionary # 1 and Dictionary # 2
    :precondition: None
    :postcondition: A list is returned with the common keys of both dictionaries
    :complexity: Best Case = Worst Case = O(n), where n is the length of the dictionary
    '''

    for key in dict1.keys():
        if key in dict2.keys():
            L.append(key)
    return L


L = []
dict1 = {'Name': 'foo', 'Age': 11, 'Class': 'First'}
dict2 = {'Name': 'bar', 'Age': 12, 'Subject': 'xyz'}

print(common_keys(dict1, dict2))
