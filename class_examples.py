'''
LEGB
    L - Local
    E - Enclosing
    G - Global
    B - Built in
'''
'''
name = "This is a global name"

def greet():
    name = "Anna"

    def hello():
        print ('Hello ' + name)
    
    hello()

greet()

'''
'''
l = [1, 2, 3]
print(type(())) # in Python everything is an object
print(type(1))
print(type({}))
print(type(l[1]))
print(type('a'))
'''
'''
class Sample():     # class names start with capital letters (also have methods and attributes)
    pass            # execute without throwing any errors

x = Sample()

print(type(x))
'''
'''
class Dog():
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sam = Dog('Labrador Retriever', "Sam")
fido = Dog('Huskie', "Fido")

print(sam.name + ", " + sam.breed)
print(fido.breed)
'''
'''
class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

c = Circle()

c.setRadius(2)
print("Radius is:", c.getRadius(), "cm")
print("Area is:", c.area(), "cm2")
'''
'''
class Animal():
    def __init__(self):
        print("Animal created")

    def WhoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def WhoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.WhoAmI()
d.eat()
d.bark()
'''

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print("A book by", author, "called", title, "has been created")

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book is destroyed!")

book = Book("Python course!", "Haithem", 169)
print(book)
print(len(book))
