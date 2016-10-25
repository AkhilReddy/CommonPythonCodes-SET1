def BubleSort(L):
    for i in range(len(L)-1):
        j = i+1
        while j < len(L):
            if L[i] > L[j]:
                #Swap
                temp = L[i]
                L[i]=L[j]
                L[j]=temp
            j += 1

def BSearch(L,low,high,e):
    if low == high:
        return L[low] == e
    #mid = low + int((high-low)/2)
    mid = int((high-low)/2)
    if L[mid] == e:
        return True
    else:
        return False
    if L[mid]<e:
        BSearch(L,mid+1,high,e)
    if L[mid]>e:
        BSearch(L,low,mid-1,e)
    
def Search(L,e):
    if len(L) == 0:
        return False
    else:
        return BSearch(L,0,len(L)-1,e)

    
L=[13,4,2,7,1,3,5,8,11]
e = 5

BubleSort(L)
print L
print Search(L,e)
    
