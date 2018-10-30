import Task_3
from Task_3 import ArrayOperations


def file_list(filename):
    '''
    This function takes a filename as an input by the user and reads the contents of the file into a list, storing each line as a single item in the list
    :param: None
    :precondition: A file must exist from which the contents of the file can be read
    :postcondition: A list is created with each line in the file stored as a single item in the list
    :complexity: Best Case = Worst Case = O(n), where n is the length of the contents in the file, even if the contents are empty or filled the loop will run n times
    '''

    infile = open(filename, 'r')
    contents = infile.readlines()
    L = ArrayOperations()
    for i in range(len(contents)):
        L.append(contents[i].rstrip('\n'))
    infile.close()
    return L

if __name__ == '__main__':

    filename = input('Enter the name of the file: ')
    print(file_list(filename))
