# instruction in animal.py

from animal import Animal

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

        
'''        

mammal = Mammal("Kurt")
print(mammal.get_name())
'''