tup = (2,4,3,6,7,8)

listi = list()

#print listi(tup)

for x in tup:
    listi.append(x)

print listi

'''

#listy = list()



level1 = (
         (1,1,1,1,1,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,1,1,1,1,1))

#print [listy(i) for i in level1]

level1 = map(listy,level1)

print level1

'''

level1 = (
         (1,1,1,1,1,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,0,0,0,0,1),
         (1,1,1,1,1,1))

print level1

listy = list()
finallist = list()

'''
for i in level1:
    for x in i:
        listy.append(x)

'''
for i in level1:
    listy = list(i)
    finallist.append(listy)


print listy
print finallist

tuplist = list()

for x in finallist:
    tupy=tuple(x)
    tuplist.append(tupy)

print tuplist

print tuple(tuplist)

sample = (1,4,6)

b = (9,6)

#c = tuple()

c = (56,)

sample = sample + b + c

print sample