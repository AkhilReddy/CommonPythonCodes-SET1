# Convert List of integers to String using ''.join


list1 = ['1', '2', '3']
str1 = ''.join(list1)

print str1

'''
if the list is of integers, convert the elements before joining them.

'''

list1 = [1, 2, 3]

'''
str1 = ''.join(str(e) for e in list1)

'''
list2 = []
for e in list1:
    list2.append(str(e))


print list2

str1 = ''.join(list2)

print str1

print type(str1)


