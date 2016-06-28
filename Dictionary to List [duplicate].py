# Dictionary to List [duplicate]

#My dictionary
dict = dict()
dict['Capital']="London"
dict['Food']="Fish&Chips"
dict['2012']="Olympics"

#lists
temp = []
dictList = []

'''
#My attempt:
for key, value in dict.iteritems():
    aKey = key
    aValue = value
    temp.append(aKey)
    temp.append(aValue)
    dictList.append(temp)
    aKey = ""
    aValue = ""

'''

for key, value in dict.iteritems():
    temp.append(key)
    dictList.append(value)

print temp
print dictList
