#-------------------------------------------------------------------------------
#
# Author:      AKHIL REDDY
#
#-------------------------------------------------------------------------------

def main():
    pass

def CommonLetters(str1, str2):
    #print str1.split()
    list1=list(''.join(str1.split()))
    return [x for x in list1 if x in str2]

if __name__ == '__main__':
    main()
#print CommonLetters('AMITABH BACHCHAN','RAJNIKANTH')

List =  CommonLetters('AMITABH BACHCHAN','RAJNIKANTH')

counts = dict()
for let in List:
    counts[let] = counts.get(let, 0 ) + 1

# print counts

for k in counts:
    print k