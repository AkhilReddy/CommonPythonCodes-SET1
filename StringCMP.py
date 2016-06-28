def isWordGuessed(secretWord, lettersGuessed):
    str = ''.join(lettersGuessed)
    if str == secretWord:
        return True
    else:
        return False


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)