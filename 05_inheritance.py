# inheritance is like family tree.A child class (or subclass) inherits traits (attributes
# and methods)from its parent class(or superclass)
# This allows you to create new classes that are specialised versions of existing classes, without rewriting all the code
    
'''
class Animal: #parent class (superclass)
    location = "germany"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic animal sound")
    
class Dog(Animal): # This is how inheritance is done in python
    def speak(self):
        print("woof!")
        
# a = Animal("Dog")
# a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)

'''

# super() : inside a child class, super() lets you call methods from the parent class.
#  This is useful when to extendthr parents behavior instead of completely replacing it.
#  its especially important when initializing the parent class's part of a child object

class Animal: #parent class (superclass)
    location = "germany"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("speaking now...")
    
class Dog(Animal): # This is how inheritance is done in python
    def speak(self):
        super().speak() # we are using the speak function of the parent class
        print("woof!")
        
# a = Animal("Dog")
# a.speak()
d = Dog("Bruno")
d.speak()
# print(d.location)
