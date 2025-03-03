#Importing Nessasary Packages:
from abc import ABC, abstractmethod

#Creating Base Class:
class Animal(ABC):

    #Abstract Method:
        #Should be implemented by all Subclasses:
        def move(self):
                pass
        
#Sub Classes:
class Human(Animal):
        def move(self):
                print('I can walk and run')

class Snake(Animal):
        def move (self):
                print('I can crawl')

class Panda(Animal):
        def move(self):
                print('I can eat bamboo')

class Dog(Animal):
        def move(self):
                print('I can bark')

class Lion(Animal):
        def move(self):
                print('I can roar')

class Elephant(Animal):
        def move(self):
                print('I can walk')

class Monkey(Animal):
        def move(self):
                print('I can jump')

class me(Animal):
        def move(self):
                print('I can do anything')
                print('HA HA HA HA HA HA HA')

#Driver Code:

H = Human()
H.move()

S = Snake()
S.move()

P = Panda()
P.move()

D = Dog()
D.move()

L = Lion()
L.move()

E = Elephant()
E.move()

M = Monkey()
M.move()

me = me()
me.move()
