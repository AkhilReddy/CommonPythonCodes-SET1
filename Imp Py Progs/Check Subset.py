def CheckSubset(L,S):
    L.sort()
    S.sort()
    
    for i in range(len(L)):
        if L[i] == S[i]:
            break
    l = len(S)
    L = L[i:i+l]
    
    print L,S
    
    for i in range(l):
        try:
            if(L[i]-S[i] != 0):
                return 1
        except IndexError:
            return 1
    return 0
    
if __name__=='__main__':
    L = [1,4,2]
    S = [1, 4, 4, 2]

    flag = CheckSubset(L,S)
    if flag is 0:
        print "S Subset of L"
    else:
        print "S Not Subset of L"
    
    
