# Testing the inherited classes - get_name exists only in the base class Animal

from lizard import Lizard
from gorilla import Gorilla
from bear import Bear
from snake import Snake

lizard1 = Lizard("Sweetiepie")
gorilla1 = Gorilla("Howard")
bear1 = Bear("Dolly")
snake1 = Snake("Hzzzz")

print(lizard1.get_name())
print(gorilla1.get_name())
print(bear1.get_name())
print(snake1.get_name())

# print(help(bear1))
help(bear1)
