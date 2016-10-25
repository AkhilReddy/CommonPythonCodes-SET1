def HashInsert(Jur,key,value):
    for i in range(len(key)):
        Jur[key[i]] = value[i]
    return

def ReverseMap(Jur):
    Rev = dict()
    for key,value in Jur.items():
        try:
            Rev[value].append(key)
        except:
            Rev[value] = [key] # To applay append() we need to use []
    return Rev

def FindStart(Jur,RevJur):
    for Key,Values in Jur.items():
        if RevJur.has_key(Key) == False:
            #print Key
            return Key

def PrintTicket(Start,Jur):
    while True:
        if Jur.has_key(Start)== False:
            return None
        print Start,'->',Jur[Start]
        Start = Jur[Start]

def EmployeeCount(Emp,RevEmp,Rec):
    for key,val in Emp.items():
        count = 0
        if RevEmp.has_key(key) == False:
            Rec[key]=count
    #print Rec
    for key,val in RevEmp.items():
        count = 0
        for i in val:
            if i == key:
                continue
            count = count + Rec[i] + 1
        Rec[key] = count
    return 
        
          

if __name__ == '__main__':
    #print 'aaa'
    #Find Itinerary from a given list of tickets
    Jur = dict()
    key = ["Chennai","Bombay","Goa","Delhi"]
    value = ["Banglore","Delhi","Chennai","Goa"]
    HashInsert(Jur,key,value)
    print '\n',Jur
    RevJur = ReverseMap(Jur)
    print '\n',RevJur

    Start = FindStart(Jur,RevJur)
    print "\n",Start
    print "\n"
    i = PrintTicket(Start,Jur)

    #Find number of Employees Under every Employee
    key = ["A","B","C","D","E","F"]
    value = ["C","C","F","E","F","F"]
    Emp = dict()
    HashInsert(Emp,key,value)
    print '\n',Emp
    RevEmp = ReverseMap(Emp)
    print '\n',RevEmp
    Rec = dict()
    EmployeeCount(Emp,RevEmp,Rec)
    print '\n',Rec

    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    

    

    
        
