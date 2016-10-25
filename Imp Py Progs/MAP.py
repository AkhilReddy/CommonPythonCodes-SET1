'''
Note:

map isn't particularly pythonic. I would recommend using list comprehensions instead:

map(f, iterable)
is basically equivalent to:

[f(x) for x in iterable]
map on its own can't do a Cartesian product, because the length of its output list is always the same as its input list. You can trivially do a Cartesian product with a list comprehension though:

[(a, b) for a in iterable_a for b in iterable_b]
The syntax is a little confusing -- that's basically equivalent to:

result = []
for a in iterable_a:
    for b in iterable_b:
        result.append((a, b))

map in Python 3 is equivalent to this:

def map(func, iterable):
    for i in iterable:
        yield func(i)


[func(i) for i in iterable]



For example, updating all the items in a list can be done easily with a for loop:

>>> items = [1, 2, 3, 4, 5]
>>> squared = []
>>> for x in items:
	squared.append(x ** 2)

	
>>> squared
[1, 4, 9, 16, 25]
>>> 
Since this is such a common operation, actually, we have a built-in feature that does most of the work for us.

The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns a list containing all the function call results.

>>> items = [1, 2, 3, 4, 5]
>>> 
>>> def sqr(x): return x ** 2

>>> list(map(sqr, items))
[1, 4, 9, 16, 25]

--------------------------------------------------------------------------------

We passed in a user-defined function applied to each item in the list. map calls sqr on each list item and collects all the return values into a new list.



Because map expects a function to be passed in, it also happens to be one of the places where lambda routinely appears:

>>> list(map((lambda x: x **2), items))
[1, 4, 9, 16, 25]
>>> 
In the short example above, the lambda function squares each item in the items list.




As shown earlier, map is defined like this:

map(aFunction, aSequence)
While we still use lamda as a aFunction, we can have a list of functions as aSequence:

def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value
Output:

[0, 0]
[1, 1]
[4, 8]
[9, 27]
[16, 64]

--------------------------------------------------------------------------------
'''


items = [1, 2, 3, 4, 5]
squared = []
for x in items:
    squared.append(x ** 2)

print squared

items = [1, 2, 3, 4, 5]

def sqr(x): return x ** 2

print map(sqr, items)

print list(map((lambda x: x **2), items))


def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value	
