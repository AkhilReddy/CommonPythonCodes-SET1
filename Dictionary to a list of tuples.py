d = { 'a': 1, 'b': 2, 'c': 3 }
print d.items()

print [(v, k) for k, v in d.iteritems()]