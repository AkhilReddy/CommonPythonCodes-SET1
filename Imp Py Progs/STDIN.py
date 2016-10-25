
L = map(str, raw_input().split())

print L

import sys
message = sys.stdin.readlines() # ctrl + d/z to stop input

print message

name = raw_input("Enter your name: ")   # Python 2.x


name = input("Enter your name: ")   # Python 3

import sys
data = sys.stdin.readlines()
print "Counted", len(data), "lines."


while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    if not line:
        break

    print line


import sys
line = sys.stdin.readline()
while line:
    print line,
    line = sys.stdin.readline()


#you are given space separated numbers in line. You can do something like:
arr = map(int, raw_input().split())

a = map(int, raw_input().strip().split(" "))

