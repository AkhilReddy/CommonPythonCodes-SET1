def SelectionSort(L):
    for i in range(len(L)-1):
        #minIndex = i
        minval = L[i]
        j = i+1
        while j < len(L):
            if minval > L[j]:
                minIndex = j
                minval = L[j]
            j += 1
        temp = L[i]
        #print minval
        L[i]= minval
        #L[i]= L[minIndex]
        L[minIndex] = temp
                    
L = [5,9,12,34,65,0,11,9,12,1]















