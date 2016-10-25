num = input("Please give the Integer : ")
numbr = num
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 2:
    result = str(num%2) + result
    num = num/2
if num <= 2:
    result = str(num/2)+ str(num%2) + result
if isNeg:
    result = '-' + result

#result = int(result)

print("Binary number of Integer "+ str(numbr) +" is "+ result)

'''
num = 100
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 2:
    result = str(num%2) + result
    num = num/2
if num <= 2:
    result = str(num/2)+ str(num%2) + result
if isNeg:
    result = '-' + result

print result
'''
