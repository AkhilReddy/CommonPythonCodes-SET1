num = input("Please give the Number :")
numbr=num
result = 0
cont = 0
while True:
    bin = num % 2
    sav = num
    num = num/2
    if num > 0:
        result += bin*(10**cont)
        cont+=1
        print result
        print "aaa\n"
    else:
        break
result += sav*(10**cont)
print("Binary number of Integer "+ str(numbr) +" is "+str(result))
    
