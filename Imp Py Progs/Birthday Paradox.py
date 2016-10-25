# Birthday Paradox

import math

x = input("Please give required probability of number of people for a given probability: ")

def find(p):
    return math.ceil(math.sqrt(2*365*math.log(1/(1-p))))

print "Total number of People with ",x*100,"% Probaility of birthday on same day",find(x)
