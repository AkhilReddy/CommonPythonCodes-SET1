print "\n\n Object Oriented Programming :- \n"

import datetime

class Car(object):

    def __init__(self,name,tyres):
        self.name = name
        self.wheels = tyres
        self.company = None
        self.release = None
        self.version = name.split(' ')[-1]

    def getVersion(self):
        return self.version

    def setCompany(self,company):
        self.company = company

    def setRelease(self,day,month,year):
        self.release = datetime.date(year,month,day)

    def verAge(self):
        if self.release == None:
            raise ValueError
        return ((datetime.date.today() - self.release).days)/365

    def __lt__(self, other): #Here other is another Object of same Class
        if self.name == other.name:
            return self.version < other.version
        return self.name < other.name

    def __str__(self):
        return self.name


ex = Car("Ford Figo1x",4)
print ex
print ex.wheels
print ex.release

print ex.version

print ex.getVersion()

ex.setRelease(9,07,1994)

print ex.release

print str(ex.verAge()) + " Years"

eg = Car("Maruthi Suzuki SX3",5)

print eg.version

objList = [ex,eg]

for p in objList:
    print p

print "\nSorting of Class Objects:"
objList.sort()

for p in objList:
    print p


################################################################################
print "\n\n Inhritance :- \n"
'''
Inheritance in Python

We are assiging Idno's to car in showroom by Inheriting Car
'''

class ShowRoom(Car): 
    #Private Viaribles
    nextId = 0 # next ID number to assign

    def __init__(self,name,tyres):#To inherit we need to have same arg in init's
        #Initalising Car Attributes
        Car.__init__(self,name,tyres)
        self.idNum = ShowRoom.nextId
        ShowRoom.nextId += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

p1 = ShowRoom('Ford Figo1x',4)
p2 = ShowRoom('Ford Fiasta',5)
p3 = ShowRoom('TATA NaNo',3)

print p1.getIdNum()
print p2.getIdNum()
print p1.name
print p1.version

print p1 < p2
print p3 < p2


################################################################################
print "\n\n Multiple Inhritance :- \n"
'''
Multiple Inheritance

'''

class Distributer(ShowRoom):
    def __init__(self,name,tyres,exp):
        ShowRoom.__init__(self,name,tyres)
        self.expirey = exp

    def getExpery(self):
        return self.expirey

class Shipping(ShowRoom):
    pass


def isStudent(obj):
    return isinstance(obj,Shipping) or isinstance(obj,Distributer)

s1 = Distributer('Ford Figo',4, 10)
s2 = Shipping('Ford Fiesta',4)
print isStudent(s1)
print isStudent(s2)
