# class Human(object):
#     def __init__(self, clan=None):
#         self.age = 18
#         self.intel = 22
#         self.strength = 44
#         self.hp = 100
#         self.clan = clan
#         print "Hello World!"
#     def taunt(self):
#         print "You want to go?!"
#
# tom = Human("tacos")
# print tom.clan
#
# class Test(object):
#     def __init__(self, phrase="hello thar"):
#         print "this was passed in: " + phrase
#         self.phrase = phrase
# test1 = Test("hey yo")
# test2 = Test()
#
# class Bike(object):
#     def __init__(self, price, max_speed):
#         self.price = price
#         self.max_speed = max_speed
#         self.miles = 0
#     def displayinfo(self):
#         print self.price
#         print self.max_speed
#         print self.miles
#     def ride(self):
#         print "Riding"
#         self.miles += 10
#         print "Increased by {}".format(self.miles)
#         return self
#     def reverse(self):
#         print "Reversing"
#         self.miles -= 5
#         if self.miles <= 0:
#             self.miles = 0
#         print "Reversed speed by {}".format(self.miles)
#         return self
# bike1 = Bike(200, "25mph")
# bike1.ride().reverse().reverse().reverse().ride().ride().displayinfo()
# class Car(object):
#     def __init__(self, price, speed, fuel, mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         if self.price > 10000:
#             self.tax = self.price * .15
#             self.price = self.price + self.tax
#         else:
#             self.tax = self.price * .12
#         self.price = self.price + self.tax
#         self.display_all()
#     def display_all(self):
#         print "Price: {} Speed: {} Fuel: {} Mileage: {} Tax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
# car1 = Car(800, 25, 22, 199)

class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health
        print self.name
        return self
cat = Animal("taco")
cat.display_health().walk().walk().run().display_health()
print "done with cat"
print "*****************"


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
pupper = Dog("zippy")
pupper.pet().walk().walk().walk().run().run().pet().display_health()
print "done with pupper"
print "*****************"

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health += 10
        return self
dragon1 = Dragon("burger")
dragon1.fly().walk().walk().walk().run().run().fly().display_health()
print "*****************"
