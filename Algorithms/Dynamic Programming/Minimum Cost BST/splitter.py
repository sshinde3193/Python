import string

def read_file(filename):
    '''
    This function takes any supplied text file and reads through each character of the file & applies specific operations on it.
    :param: Any supplied text file
    :precondition: The text file must be provided by the user
    :postcondition: The file has been read, with specific operations applied on them and stored in a list
    :return: A list is returned with the contents of the file without any punctuation (all converted to blank space) and all characters in uppercase
    :complexity: Best Case = Worst Case = O(n), where n is the number of total characters (length of total contents)
    '''

    text_list = []
    file_r = open(filename, 'r')
    contents = file_r.read()
    for character in range(len(contents)):
        text_list.append(contents[character].upper())
        if text_list[character] not in string.ascii_uppercase:
            text_list[character] = ' '
    return text_list

def split_text_to_words(filename):
    '''
    This function splits the resultant transformed text into words (split on blankspace)
    :param: Any supplied text file
    :precondition: The file must be provided by the user and read_file function must exist
    :postcondition: The text is joined into words & split on the blankspace & all words except single letters and spaces are appened into a new list
    :return: A final word list is returned which is split on the blankspace which does not contain any single letters or spaces
    :complexity: Best Case = Worst Case = O(n), where n is the length of the temp word_list
    '''

    text_list = read_file(filename)
    temp_word_list = ''.join(text_list)
    temp_word_list = temp_word_list.split(' ')
    final_word_list = []
    for j in range(len(temp_word_list)):
        if len(temp_word_list[j]) > 1:
            final_word_list.append(temp_word_list[j])
    return final_word_list

def write_file(filename):
    '''
    This function writes all the split words into an output file splitwords.txt, ignoring all single letter words
    :param: Any supplied text file
    :precondition: None
    :postcondition: The split words are written into an output file
    :return: None
    :complexity: Best Case = Worst Case = O(n), where n is the length of the word_list
    '''

    final_word_list = split_text_to_words(filename)
    file = open('splitwords.txt', 'w')
    for i in range(len(final_word_list)):
        file.write(final_word_list[i] + '\n')


if __name__ == '__main__':
    filename = input('Enter the filename: ')
    write_file(filename)
