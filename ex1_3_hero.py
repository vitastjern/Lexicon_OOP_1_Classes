# Create a class called Hero. Upon initialization it should receive a name(string) and health(number).
# Create two functions:
#   -defend(damage) -   Deal the given damage to the hero; if the health is 0 or less, set it to 0
#                       and return "{name} was defeated".
#   -heal(amount) -     Increase the health of the hero with the given amount.
#

class Hero():
    def __init__(self, name:str, health:int):
        self.name = name
        self.health = health
        # print("Hero was created")

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'
        else:
            return None
            # I like the line below better as a return value compared to using None... ;)
            # return f'{self.name} was hit with {damage} damage, their health is now at {self.health}'
    
    def heal(self, amount):
        self.health += amount
        # print(f'{self.name} was healed {amount} points, their health is now as {self.health}')


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))


