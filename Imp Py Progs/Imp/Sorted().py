class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "<name: %s, age: %s>" % (self.name, self.age)

jack = Person('Jack', 19)
adam = Person('Adam', 43)
becky = Person('Becky', 11)

people = [jack, adam, becky]

u = sorted(people)
print u

def byName_key(person):
    return person.name

v = sorted(people,key = byName_key)
print v

from operator import attrgetter

getName = attrgetter('name')
print getName(jack)

w = sorted(people, key = attrgetter('name'))
print w

x = sorted(people, key = attrgetter('age'))
print x

class Snake(object):
      def __init__(self, name, toxicity, aggression):
              self.name = name
              self.toxicity = toxicity
              self.aggression = aggression
      def __repr__(self):
              return "<%s>" % self.name

gardenSnake = Snake('gardenSnake', 10, 0.1)
rattleSnake = Snake('rattleSnake', 100, 0.25)
kingCobra = Snake('kingCobra', 50, 1.0)
snakes = [rattleSnake, kingCobra, gardenSnake]

def byDangerous_key(snake):
    return snake.toxicity * snake.aggression


y = sorted(snakes, key = byDangerous_key)
print y

from random import random

def randomOrder_key(element):
    return random()

z = sorted(snakes, key = randomOrder_key)
print z

'''
Lamda
'''
s = sorted(people, key=lambda x:x.age) # same as KeybyAge
print s









