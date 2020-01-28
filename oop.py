# class- blueprint; (description of a future object)
# object-instances of class-
# syntax class: e.g class Car: (use title case for first letter in a word)
# OOP-programming approach(recipe type of programming)- programming paradigm

# class attribute(global)
# instance attribute (specific to that object)
# creating a class

class Car:
    pass
# car1= Car()
# car2= Car()
# car3= Car()
# car4= Car()
# car5= Car()
#
# print(type(car1))
#
# # class attribute
# make='Toyota'
#
# car1= Car()
# car2= Car()
# xyz= Car()
#
# # car1,car2,xyz are all toyotas coz they have been defined as make
#
# print(car1.make)
# car2= Car()
# print(car2.make)
#
# # object properties/attribute
# car1.yom = 2012
# car2.yom = 2018
# # check yr of manufacture
# print(car1.yom)
# print(car2.yom)

# model a laptop. hp, ram, hardisk, screen size

# class Laptop:
#     type='hp'
#
#
#     def switchOn(self):
#         print('------LOADING-----')
#
#
#     def switchOff(self):
#          print('----Shutting Down-----')
#
# elitebook = Laptop()
# elitebook.ram='4GB'
# elitebook.hdd='256GB'
# elitebook.sz='14 inch'
#
# print(elitebook.type)
# print(elitebook.ram)
#
# pavilion = Laptop()
# pavilion.ram='4GB'
# pavilion.hdd='256GB'
# pavilion.sz='14 inch'
#
# envy = Laptop()
# envy.ram='4GB'
# envy.hdd='256GB'
# envy.sz='14 inch'
#
#
# probook = Laptop()
# probook.ram='4GB'
# probook.hdd='256GB'
# probook.sz='14 inch'
#
# # switch on (self is a convention)
# elitebook.switchOn()
# elitebook.switchOff()

# constructor (once an instance has been created, can have any number of variables you would like)
class Person:

    def __int__(self, name, age, kgs):
        self.theName = name
        self.theAge = age
        self.theKgs = kgs
    def updateAge(self,newAge):
        self.theAge = newAge

june = Person('June',16,55)
print('initial age:',june.theAge)
june.updateAge(19)
print('Current Age:',june.newAge)

ryan = Person('Ryan',20,60)
print('initial age:', ryan.theAge)

# principleof OOP
# inheritance
# abstraction
# poly-morphisim
# encapsulation


