aString = 'foofoo'

def double_word(aString):
    result = True
    if len(aString) % 2 != 0:
        result = False
    first_word = aString[0:len(aString)//2]
    second_word = aString[len(aString)//2:]
    for i in range(len(aString)//2):
        if first_word[i] != second_word[i]:
            result = False


    return result


print(double_word(aString))
