# Polymorphism example

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow!")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Woff!")

cat1 = Cat("Kitty", 3)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()     # we got the same function names in the Cat and Dog
    animal.info()           # classes, that is why it works for all animal
    animal.make_sound()     # objects, regardless if it is a Cat or a Dog...

