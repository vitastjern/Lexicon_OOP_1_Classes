# Task ZOO:
# Follow the diagram and creat all of the classes. Each of them, except the Animal class, should inherit
# from another class.
# The Animal class should have attribute name - string and getter for the name.
# Every class should have a constructor, which accepts one parameter: name.

# things are called from zoo.py

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)
