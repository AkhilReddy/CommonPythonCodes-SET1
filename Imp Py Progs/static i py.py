x=0

def static_num() :
   global x
   x=x+1
   return x


for i in range(0,10) :
     print static_num()
