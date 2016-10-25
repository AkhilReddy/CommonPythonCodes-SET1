def Permutate(L,a,l,f):
    if l == f:
        d = ''.join(a)
        #print d
        L.append(d)
    else:
        for i in xrange(l,f+1):
            a[l],a[i] = a[i],a[l]
            Permutate(L,a,l+1,f)
            a[l],a[i] = a[i],a[l] # Backtracking
    
s = raw_input()
print s
l = len(s)
a = list(s)
L = []

Permutate(L,a,0,l-1)

print L 


