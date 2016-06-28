import string

def getCommonLetters(text1, text2):
    text1List = text1.split()
    text2List = text2.split()
    for i in range(0, len(text1List)):
        text1List[i] = getCleanText(text1List[i])
    for i in range(0, len(text2List)):
        text2List[i] = getCleanText(text2List[i])

    outList = []
    for letter in text1List:
        if letter in text2List and letter not in outList:
           outList.append(letter)
    return outList

def getCleanText(text):
    text = text.lower()

    badCharacters = string.whitespace + string.punctuation
    for character in badCharacters:
        text = text.replace(character, "")
    return text

userText1  = raw_input("Enter your first name: ")
userText2  = raw_input("Enter your last name: ")
result     = getCommonLetters(userText1, userText2)
numMatches = len(result)
if numMatches == 0:
    print "No matches."
else:
    print "Number of matches:", numMatches

for letter in result:
    print letter