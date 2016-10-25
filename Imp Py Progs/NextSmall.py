def nextsmall(N,LL):
    c = 0
    j = 0
    for i in LL:
        n = N-i
        if n <= 0 :
            j +=1
            continue
        elif c == 0:
            min = n
            k = j
        else:
            if min > n:
                min = n
                k = j
        c +=1
        j +=1
    return LL[k]

def suffix(LL):
    min = LL[0]
    c = 0
    for i in LL[1:]:
        if not min-i:
            break
        c +=1
    return LL[:c],LL[c:]

def suffixdivider(L):
    L1=[]
    L1.extend(L)
    L2 = []
    L.sort()
    L2.extend(L)
    #print L1,L2
    for i in range(len(L)):
        if L2[i]-L1[i]<0:
            return L1[:i],L1[i:]
    return L1,[0]

LL = [1,2,3,6,5,4]
N = 4
print nextsmall(N,LL)
a,b = suffix(LL)

print a,b
k = b[0]
print nextsmall(k,LL)
##########3
LL = [1,2,3,6,5,4]
M = []
M.extend(LL)
c,d = suffixdivider(LL)

print c,d

x = max(c)
print x

y = min(d)
print y

i1 = M.index(x)
i2 = M.index(y)

print M
print i1,i2

i11 = c.index(x)
i21 = d.index(y)

print i11,i21

temp = c[i11]
c[i11] = d[i21]
d[i21] = temp

print c,d

d.reverse()
print c,d

c.extend(d)

print c


