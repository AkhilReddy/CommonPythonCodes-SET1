def removeDups(L1, L2):
    for e1 in L1:
        #print e1
        if e1 in L2:
            L1.remove(e1)


L1 = [1,2,3,4]
L2 = [1,2,5,6]
if 2 in L2:
    print True
removeDups(L1, L2)
print(L1)


def removeDupsBetter(L1, L2):
    L1Start = L1[:] #only way to copy full list without any effect of furthur changes to L1 effecting 
#L1Srart
    #L1Start = L1
    for e1 in L1Start:
        print L1Start
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)
