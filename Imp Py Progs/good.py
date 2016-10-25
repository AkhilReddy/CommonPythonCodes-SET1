import operator

#How to conditionally replace items in a list

mylist = [111, -222, 333, -444]
newlist = []
for item in mylist:
    if item < 0:
        item = 0
    newlist.append(item)
mylist = newlist
print mylist

mylist = [111, -222, 333, -444]
for (i, item) in enumerate(mylist):
    if item < 0:
        mylist[i] = 0
print mylist

mylist = [111, -222, 333, -444]
mylist = [x*(x>=0) for x in mylist]
print mylist

mylist = [111, -222, 333, -444]
print map(lambda x: 0 if x<0 else x, mylist)

mylist = [111, -222, 333, -444]
print [ 0 if x < 0 else x for x in mylist ]
 
#Python setdefault example

DATA_SOURCE = (('key1', 'value1'),
               ('key1', 'value2'),
               ('key2', 'value3'),
               ('key2', 'value4'),
               ('key2', 'value5'),)

newdata = {}
for k, v in DATA_SOURCE:
    if newdata.has_key(k):
        newdata[k].append(v)
    else:
        newdata[k] = [v]
print newdata

for k in DATA_SOURCE:
    print k

for k, v in DATA_SOURCE:
    print k,v

#Better way using setdefault:

newdata = {}
for k, v in DATA_SOURCE:
    newdata.setdefault(k, []).append(v)
print newdata

from collections import defaultdict
newdata = defaultdict(list)
DATA_SOURCE = (('key1', 'value1'),
           ('key1', 'value2'),
           ('key2', 'value3'),
           ('key2', 'value4'),
           ('key2', 'value4'),)
for k, v in DATA_SOURCE: newdata[k].append(v)

print newdata

#How to sort a list of dicts in Python

from pprint import pprint

DATA = [
    {u'avg': 2.9165000000000001,
     u'count': 10.0,
     u'total': 29.165000000000003,
     u'ups_ad': u'10.194.154.49:80'},
    {u'avg': 2.6931000000000003,
     u'count': 10.0,
     u'total': 26.931000000000001,
     u'ups_ad': u'10.194.155.176:80'},
    {u'avg': 1.9860909090909091,
     u'count': 11.0,
     u'total': 21.847000000000001,
     u'ups_ad': u'10.195.71.146:80'},
    {u'avg': 1.742818181818182,
     u'count': 11.0,
     u'total': 19.171000000000003,
     u'ups_ad': u'10.194.155.48:80'}
    ]

data_sorted = sorted(DATA, key=lambda item: item['ups_ad'])
pprint(data_sorted)
'''
data_sorted2 = sorted(DATA, key=operator.itemgettr('ups_ad'))
print data_sorted2
'''
#An example using Python's groupby and defaultdict to do the same task

SOME_DATA = [
    {'model': u'Yaris', 'some_value': 11202, 'trim_name': u'3-Door L Manual'},
    {'model': u'Yaris', 'some_value': 19269, 'trim_name': u'3-Door LE Automatic'},
    {'model': u'Corolla', 'some_value': 27119, 'trim_name': u'L Automatic'},
    {'model': u'Corolla', 'some_value': 32262, 'trim_name': u'LE'},
    {'model': u'Corolla', 'some_value': 37976, 'trim_name': u'S Premium'},
    {'model': u'Camry', 'some_value': 39730, 'trim_name': u'LE 4-Cyl'},
    {'model': u'Camry', 'some_value': 45761, 'trim_name': u'XSE 4-Cyl'},
    {'model': u'Yaris', 'some_value': 48412, 'trim_name': u'3-Door L Automatic'},
    {'model': u'Camry', 'some_value': 55423, 'trim_name': u'XLE 4-Cyl'},
    {'model': u'Corolla', 'some_value': 57055, 'trim_name': u'ECO Premium'},
    {'model': u'Corolla', 'some_value': 61296, 'trim_name': u'ECO Plus'},
    {'model': u'Camry', 'some_value': 63660, 'trim_name': u'XSE V6'},
    {'model': u'Yaris', 'some_value': 65570, 'trim_name': u'5-Door LE Automatic'},
    {'model': u'Camry', 'some_value': 67461, 'trim_name': u'XLE V6'},
    {'model': u'Corolla', 'some_value': 73602, 'trim_name': u'S'},
    {'model': u'Yaris', 'some_value': 74158, 'trim_name': u'5-Door SE Manual'},
    {'model': u'Corolla', 'some_value': 74249, 'trim_name': u'LE Plus'},
    {'model': u'Corolla', 'some_value': 78386, 'trim_name': u'ECO'},
    {'model': u'Camry', 'some_value': 82747, 'trim_name': u'SE 4-Cyl'},
    {'model': u'Corolla', 'some_value': 83162, 'trim_name': u'LE Premium'},
    {'model': u'Corolla', 'some_value': 84863, 'trim_name': u'S Plus Manual'},
    {'model': u'Yaris', 'some_value': 90313, 'trim_name': u'5-Door L Automatic'},
    {'model': u'Corolla', 'some_value': 90452, 'trim_name': u'L Manual'},
    {'model': u'Yaris', 'some_value': 93152, 'trim_name': u'5-Door SE Automatic'},
    {'model': u'Corolla', 'some_value': 94973, 'trim_name': u'S Plus CVT'},
]

import collections

grouped = collections.defaultdict(list)
for item in SOME_DATA:
    grouped[item['model']].append(item)

for model, group in grouped.items():
    print
    print model
    pprint(group, width=150)

import itertools

def keyfunc(x):
    return x['model']

SOME_DATA = sorted(SOME_DATA, key=keyfunc)
for model, group in itertools.groupby(SOME_DATA, keyfunc):
    print
    print model
    pprint(list(group), width=150)

###########################
#How to sort a dict by keys

mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key in sorted(mydict.iterkeys()):
    print "%s: %s" % (key, mydict[key])

#2:
mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

keylist = mydict.keys()
keylist.sort()
for key in keylist:
    print "%s: %s" % (key, mydict[key])

#How to sort a dict by value

for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)


mydict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}

print ('Sort by keys:')
for key in sorted(mydict.keys()):
    print ("%s: %s" % (key, mydict[key]))

print ('Sort by items:')
for key, value in sorted(mydict.items(), key=lambda item: (item[1], item[0])):
    print ("%s: %s" % (key, value))































