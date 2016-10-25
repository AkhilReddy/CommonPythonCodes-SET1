import operator

compare = operator.lt

L = [3,5,2,78,11,23,2,1,3,1,56,7,10,9,1,9]

def MergeSort(L): #def MergeSort(L,compare)
    if len(L)< 2:
        return L
    else:
        middle = int(len(L)/2)
       # left = MergeSort(L[:middle],compare)
       # right = MergeSort(L[middle:],compare)
        left = MergeSort(L[:middle])
        right = MergeSort(L[middle:])
       # return Merge(left,right,compare)
        return Merge(left,right)

def Merge(left,right): # def Merge(left,right,compare)
    result = []
    i,j=0,0
    while i<len(left) and j<len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# print MergeSort(L,compare)
print MergeSort(L)


            
          


        
    
    
