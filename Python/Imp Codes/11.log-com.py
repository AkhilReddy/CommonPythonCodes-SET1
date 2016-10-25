def intToStr(i):
    global count
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i/10
        count+=1
    return result

count = 0
s = intToStr(7777777777777777777777777777)
print count























