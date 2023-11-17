class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animals can eat.")

    def sleep(self):
        print("They can sleep during the day and night. Name:", self.name)

class Dog(Animal):
    def bark(self):
        print("Dogs can bark.")


animal1 = Animal("Elephant")
animal1.eat()
animal1.sleep()

animal2 = Animal("Lion")
animal2.eat()
animal2.sleep()

dog1 = Dog("Buddy")
dog1.eat()
dog1.sleep()
dog1.bark()