#Importing Nessary modules
from abc import ABC, abstractmethod

#Creating Base Class
class Absclass(ABC):
    
    #Function to print a value
    def print(self, x):
        print('Passed Value: ', x)

    #Abstract Method
    @abstractmethod
    def task(self):
        print('We are inside a Absclass Task')

#Creating Subclass
class test_class(Absclass):
    def task(self):
        print('We are inside a test_class Task')

#Creating Object of Subclass
test = test_class()
test.task()
test.print(100)
test.task()

#Creating Object of Base Class
a = Absclass()
a.task()
