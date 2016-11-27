ActivePython 2.7.10.12 (ActiveState Software Inc.) based on
Python 2.7.10 (default, Aug 21 2015, 14:42:12) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'abcdefghij'
>>> s
'abcdefghij'
>>> s.center(3)
'abcdefghij'
>>> s.count('cd')
1
>>> s.count('sdf')
0
>>> s.endswith('j')
True
>>> s.find('de)
       
SyntaxError: EOL while scanning string literal
>>> s.find('de')
3
>>> #It gives index of substring
>>> s.find('asd')
-1
>>> #So not a substring in s
>>> 
>>> s.index('de')
3
>>> s.index('asd')

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.index('asd')
ValueError: substring not found
>>> s.isalnum()
True
>>> s.isdigit()
False
>>> s.join('asd')
'aabcdefghijsabcdefghijd'
>>> #joins each of s with 'a','s','d'
>>> 
>>> s.partition('s')
('abcdefghij', '', '')
>>> s
'abcdefghij'
>>> x = s.join('asd')
>>> x
'aabcdefghijsabcdefghijd'
>>> x.partition('s')
('aabcdefghij', 's', 'abcdefghijd')
>>> x
'aabcdefghijsabcdefghijd'
>>> x.replace(s,'0')
'a0s0d'
>>> s
'abcdefghij'
>>> inp = 'AKHIL LITHIN REDDY'
>>> inp.split(' ')
['AKHIL', 'LITHIN', 'REDDY']
>>> inp
'AKHIL LITHIN REDDY'
>>> d = inp.split(' ')
>>> d
['AKHIL', 'LITHIN', 'REDDY']
>>> out = '  AKHIL    LITIN   REDDDY  '
>>> out
'  AKHIL    LITIN   REDDDY  '
>>> f = out.strip(' ')
>>> f
'AKHIL    LITIN   REDDDY'
>>> d = f.split(' ')
>>> d
['AKHIL', '', '', '', 'LITIN', '', '', 'REDDDY']
>>> #So use strip and split simultaneously
>>> 
>>> e = out.strip(' ')
>>> e = out.strip(' ').split(' ')
>>> e
'AKHIL    LITIN   REDDDY'
>>> e = out.strip(' ').split(' ')
>>> e
['AKHIL', '', '', '', 'LITIN', '', '', 'REDDDY']
>>> s.startswith()

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
>>> 
KeyboardInterrupt
>>> s.startswith('a')
True
>>> s.upper()
'ABCDEFGHIJ'
>>> 
