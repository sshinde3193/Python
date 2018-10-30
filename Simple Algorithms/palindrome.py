aString = 'abba'

def isPalindrome(aString):
    result = True
    if len(aString) > 1:
        for i in range(len(aString)//2):
            if aString[i] != aString[-i-1]:
                result = False
        return result

print(isPalindrome(aString))
