# Union and Intersection of LL
a = [10,15,4,20]
b = [8,4,2,10]

def InterSect(a,b):
    a.sort()
    b.sort()
    return([i for i in a if i in b])

def Substraction(a,b):
    a.sort()
    b.sort()
    return([i for i in a if i not in b])

def Union(x,y):
    x.sort()
    y.sort()
    #print a
    c = list()
    c.extend(x)
    #print c
    c.extend(y)
    #print a,b,c
    #a.remove(i for i in c if i in b)
    #print InterSect(c,b)
    for i in InterSect(x,y):
        c.remove(i)
    return(c)

def InterSect2(x,y):# Linearly scan Implementation after Sorting
    x.sort()
    y.sort()
    #print x,y
    i,j = 0,0
    c = list()
    #while (i in range(len(a))< len(a) and j in range(len(b))<len(b)):
        #print i,j
    #for i in range(a) and j in range(b):
    while i<len(x) and j < len(y):
        if x[i]<y[j]:
            i+=1
        elif y[j]<x[i]:
            j+=1
        elif x[i]==y[j]:
            c.append(y[j])
            i+=1
    return c
    
print 'a :',a,'b: ',b
print 'Intersection of a and b: ',InterSect(a,b)
print a,b
print 'Union of a and b: ',Union(a,b)
print a,b
print ' a - b: ',Substraction(a,b)
print a,b
print 'Intersection of a and b: ',InterSect2(a,b)
