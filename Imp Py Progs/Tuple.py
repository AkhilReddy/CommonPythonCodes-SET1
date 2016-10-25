#Tuple append
a = ('2',)
b = 'z'
new = a + (b,)
print new
#From tuple to list to tuple :

a = ('2',)
b = 'b'

l = list(a)
l.append(b)

l = tuple(l)

print l
#Or with a longer list of items to append

a = ('2',)
items = ['o', 'k', 'd', 'o']

l = list(a)

for x in items:
    l.append(x)

print tuple(l)

'''
The point here is: List is a mutable sequence type.
So you can change a given list by adding or removing elements.
Tuple is an immutable sequence type. You can't change a tuple.
So you have to create a new one.
'''
#Insert in Tuple
#You can cast it to a list, insert the item, then cast it back to a tuple.

a = ('Product', '500.00', '1200.00')
a = list(a)
a.insert(3, 'foobar')
a = tuple(a)
print a



