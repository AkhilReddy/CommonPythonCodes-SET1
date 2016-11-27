ActivePython 2.7.10.12 (ActiveState Software Inc.) based on
Python 2.7.10 (default, Aug 21 2015, 14:42:12) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = ['a','b','c',22,3]
>>> a[2:]
['c', 22, 3]
>>> x = a[3:]
>>> x
[22, 3]
>>> y = a[1:4]
>>> y
['b', 'c', 22]
>>> a.
SyntaxError: invalid syntax
>>> a.append(56)
>>> a
['a', 'b', 'c', 22, 3, 56]
>>> a.count(3)
1
>>> s = '123654'
>>> s
'123654'
>>> b = list(s)
>>> b
['1', '2', '3', '6', '5', '4']
>>> z = ''.join(b)
>>> z
'123654'
>>> l = len(a)
>>> l
6
>>> range(l)
[0, 1, 2, 3, 4, 5]
>>> v = range(l)
>>> v
[0, 1, 2, 3, 4, 5]
>>> a.extend(100)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.extend(100)
TypeError: 'int' object is not iterable
>>> #So extend require only another list
>>> '''

This is used for multiline Quote
'''
'\n\nThis is used for multiline Quote\n'
>>> range(l-1)
[0, 1, 2, 3, 4]
>>> a.extend(v)
>>> a
['a', 'b', 'c', 22, 3, 56, 0, 1, 2, 3, 4, 5]
>>> a.count()

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>>  a.count(1)
 
  File "<pyshell#31>", line 1
    a.count(1)
    ^
IndentationError: unexpected indent
>>> a.count(1)
1
>>> a = v
>>> a
[0, 1, 2, 3, 4, 5]
>>> # We Can equate to lists to copy one another but change in one effects other
>>> v.pop()
5
>>> v
[0, 1, 2, 3, 4]
>>> a
[0, 1, 2, 3, 4]
>>> # So a is also changed
>>> #So to Solve it,use extend
>>> a = []
>>> a
[]
>>> a.extend(v)
>>> a
[0, 1, 2, 3, 4]
>>> v.pop()
4
>>> v
[0, 1, 2, 3]
>>> a
[0, 1, 2, 3, 4]
>>> a.index(3)
3
>>> #So we get Index of element in list by this
>>> a.index(10)

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.index(10)
ValueError: 10 is not in list
>>> a.insert(3,5)
>>> a
[0, 1, 2, 5, 3, 4]
>>> #insert in to some position without disturbing original element
>>> a[3]=6
>>> a
[0, 1, 2, 6, 3, 4]
>>> #Use Indexing to disturb list
>>> p = a.pop()
>>> p
4
>>> a
[0, 1, 2, 6, 3]
>>> #This is POP
>>> #We USE it make implementation of Stack
>>> a.remove(0)
>>> a
[1, 2, 6, 3]
>>> #It removes perticular value in list
>>> a.remove(10)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.remove(10)
ValueError: list.remove(x): x not in list
>>> a.reverse()
>>> a
[3, 6, 2, 1]
>>> #Reverse is defined only for list
>>> s = 'abcdefghijkl'
>>> s
'abcdefghijkl'
>>> c = list(s)
>>> c
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
>>> c.reverse()
>>> c
['l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
>>> ss = ''.join(c)
>>> ss
'lkjihgfedcba'
>>> #This is reversing string
>>> s[-1]
'l'
>>> #Gets only last element
>>> a.sort()
>>> a
[1, 2, 3, 6]
>>> d = a.sort()
>>> d
>>> #Sorted list cannot be directly copied to another list
>>> d =[]
>>> d.extend(a)
>>> d
[1, 2, 3, 6]
>>> s[::-1]
'lkjihgfedcba'
>>> b = a.reverse()
>>> b
>>> b =[]
>>> b.extend(a.reverse())

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    b.extend(a.reverse())
TypeError: 'NoneType' object is not iterable
>>> V

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    V
NameError: name 'V' is not defined
>>> a.count(1)
1
>>> a.reverse()
>>> b.extend(a)
>>> b
[6, 3, 2, 1]
>>> 
