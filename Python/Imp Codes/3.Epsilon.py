x = 2
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
#while (abs(ans**2 - x)) >= epsilon and ans <= x:
while (abs(ans**2 - x)) >= epsilon:
    ans += step
    numGuesses += 1
    #print ans
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))


