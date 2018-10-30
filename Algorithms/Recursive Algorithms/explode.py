def explode(word):
    '''
    Adds space between each letter
    '''
    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])


string = 'foobar'
print(explode(string))
