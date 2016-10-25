def Subset(L,S):
    D = list()
    D.extend(L)
    D.extend(S)
    print D
    x = max(D)

    H1 = dict()

    for i in L:
        try:
            H1[i%x].append(1)
        except:
            H1[i%x] = [1]
    print H1

    H2 = dict()
    for i in S:
        try:
            H2[i%x].append(1)
        except:
            H2[i%x] = [1]
    print H2

    

L = [11, 1, 13, 21, 3, 3,7]
S = [11, 30, 7, 1]

Subset(L,S)





