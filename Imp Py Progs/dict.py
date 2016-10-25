
>>> a = {'a':1,'b':[2,3,4],'c':[22],23:[2,34]}
>>> a
{'a': 1, 'c': [22], 'b': [2, 3, 4], 23: [2, 34]}
>>> b = {c:23}

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b = {c:23}
NameError: name 'c' is not defined
>>> b = {'d':23,'c':223,'e':[234,34,45]}
>>> b
{'c': 223, 'e': [234, 34, 45], 'd': 23}
>>> cmp(a,b)
1
>>> # a>b
>>> dict1 = {'Name': 'Zara', 'Age': 7}; 
dict2 = {'Name': 'Mahnaz', 'Age': 27}; 
dict3 = {'Name': 'Abid', 'Age': 27}; 
dict4 = {'Name': 'Zara', 'Age': 7};
>>> print "Return Value : %d" %  cmp (dict1, dict2)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print "Return Value : %d" %  cmp (dict1, dict2)
NameError: name 'dict2' is not defined
>>> dict2 = {'Name': 'Mahnaz', 'Age': 27};
>>> dict3 = {'Name': 'Abid', 'Age': 27};
>>> dict4 = {'Name': 'Zara', 'Age': 7};
>>> print "Return Value : %d" %  cmp (dict1, dict2)
Return Value : -1
>>> print "Return Value : %d" %  cmp (dict2, dict3)
Return Value : 1
>>> print "Return Value : %d" %  cmp (dict1, dict4)
Return Value : 0
>>> dict = {'Name': 'Zara', 'Age': 7};
>>> print "Length : %d" % len (dict)
Length : 2
>>> print "Equivalent String : %s" % str (dict)
Equivalent String : {'Age': 7, 'Name': 'Zara'}
>>> print "Start Len : %d" %  len(dict)
Start Len : 2
>>> dict.clear() 
print "End Len : %d" %  len(dict)
>>> print "End Len : %d" %  len(dict)
End Len : 0
>>> dict = {'Name': 'Zara', 'Age': 7};
>>> dict2 = dict.copy()
>>> dict2
{'Age': 7, 'Name': 'Zara'}
>>> seq = ('name', 'age', 'sex')
>>> type(seq)
<type 'tuple'>
>>> dict = dict.fromkeys(seq)
>>> dict
{'age': None, 'name': None, 'sex': None}
>>> dict2 = dict.fromkeys(seq, 10)
>>> dict
{'age': None, 'name': None, 'sex': None}
>>> dict2
{'age': 10, 'name': 10, 'sex': 10}
>>> dict = {'Name': 'Zara', 'Age': 27}
>>>  dict.get('Age')
 
  File "<pyshell#32>", line 1
    dict.get('Age')
    ^
IndentationError: unexpected indent
>>> dict.get('Age')
27
>>> dict.get('Sex', "NoSex")
'NoSex'
>>> dict.has_key('Age')
True
>>> dict.has_key('Sex')
False
>>> dict.items()
[('Age', 27), ('Name', 'Zara')]
>>> #The method items() returns a list of dict's (key, value) tuple pairs
>>> x = dict.items()
>>> x
[('Age', 27), ('Name', 'Zara')]
>>> x[0]
('Age', 27)
>>> x[0].index()

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    x[0].index()
TypeError: index() takes at least 1 argument (0 given)
>>> x[0].index(1)

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x[0].index(1)
ValueError: tuple.index(x): x not in tuple
>>> x[0].index((0))

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x[0].index((0))
ValueError: tuple.index(x): x not in tuple
>>> x[0].index(27)
1
>>> x[0].index('Age')
0
>>> x[0].
SyntaxError: invalid syntax
>>> x[0].count()

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x[0].count()
TypeError: count() takes exactly one argument (0 given)
>>> x[0].count(2)
0
>>> x = dict.items()
>>> x
[('Age', 27), ('Name', 'Zara')]
>>> for i in x[0]:
	print i

	
Age
27
>>> x[0][0]
'Age'
>>> dict.keys()
['Age', 'Name']
>>> dict.setdefault(key, default=None)

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict.setdefault(key, default=None)
NameError: name 'key' is not defined
>>> dict.setdefault('Age', default=None)

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict.setdefault('Age', default=None)
TypeError: setdefault() takes no keyword arguments
>>> dict.setdefault('Age', default=None)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict.setdefault('Age', default=None)
TypeError: setdefault() takes no keyword arguments
>>> dict.setdefault('Age',None)
27
>>> #The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.
>>> dict
{'Age': 27, 'Name': 'Zara'}
>>> dict.setdefault('Sex',None)
>>> dict
{'Age': 27, 'Name': 'Zara', 'Sex': None}
>>> dict2 = {'Sex': 'female' }
>>> dict.update(dict2)
>>> dict
{'Age': 27, 'Name': 'Zara', 'Sex': 'female'}
>>> dict.values()
[27, 'Zara', 'female']
>>> animals = {}
animals["monkey"] = 1
animals["tuna"] = 2
animals["giraffe"] = 4

>>> animals
{}
>>> animals["monkey"] = 1
>>> animals["tuna"] = 2
>>> animals["giraffe"] = 4
>>> animals
{'tuna': 2, 'giraffe': 4, 'monkey': 1}
>>> if "tuna" in animals:
    print("Has tuna")
else:
    print("No tuna")

    
Has tuna
>>> # Use in on nonexistent key.
if "elephant" in animals:
    print("Has elephant")
else:
    print("No elephant")

No elephant

>>> hits = {"home": 125, "sitemap": 27, "about": 43}
>>> keys = hits.keys()
>>> values = hits.values()

>>> keys
['home', 'about', 'sitemap']
>>> values
[125, 43, 27]
>>> hits
{'home': 125, 'about': 43, 'sitemap': 27}
>>> # Sort the keys from the dictionary.
keys = sorted(hits.keys())
>>> keys
['about', 'home', 'sitemap']
>>> sorted(hits)
['about', 'home', 'sitemap']
>>> aki = sorted(hits)
>>> aki
['about', 'home', 'sitemap']
>>> plants = {"radish": 2, "squash": 4, "carrot": 7}
>>> # Loop over dictionary directly.
# ... This only accesses keys.
for plant in plants:
    print(plant)

    
radish
carrot
squash
>>> systems = {"mac": 1, "windows": 5, "linux": 1}

>>> # Remove key-value at "windows" key.
del systems["windows"]
>>> systems
{'mac': 1, 'linux': 1}
>>> # Create list of tuple pairs.
# ... These are key-value pairs.
pairs = [("cat", "meow"), ("dog", "bark"), ("bird", "chirp")]
>>> lookup = dict(pairs)

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    lookup = dict(pairs)
TypeError: 'dict' object is not callable
>>> ok = dict(pairs)

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    ok = dict(pairs)
TypeError: 'dict' object is not callable
>>> for key in plants:
	print key

	
radish
carrot
squash
>>> for key in plants:
	print key,plants[key]

	
radish 2
carrot 7
squash 4
>>> letters = "abcabcdefghi"
>>> for c in letters:
	print c

	
a
b
c
a
b
c
d
e
f
g
h
i
>>> frequencies = {}
for c in letters:
	
>>> frequencies = {}for c in letters:
	
SyntaxError: invalid syntax
>>> for c in letters:
	frequencies[c] = frequencies.get(c, 0) + 1

	
>>> frequencies
{'a': 2, 'c': 2, 'b': 2, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1}
>>> for i in frequencies.items():
	print i

	
('a', 2)
('c', 2)
('b', 2)
('e', 1)
('d', 1)
('g', 1)
('f', 1)
('i', 1)
('h', 1)
>>>my_dictionary = {'hello': 1, 'goodbye': 2}


