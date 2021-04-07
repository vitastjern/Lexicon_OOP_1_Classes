# Create a class called Shop. Upon initialization it should receive a name(string) and 
# items(list). Create a method called get_items_count() which should return the amount of 
# items in the store.
# Example:
# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())
# Should give the output: 3

class Shop():
    def __init__(self, name: str, items:list):
        self.name = name
        self.items = items
        #print("A shop has been created")

    def get_items_count(self):
        return(len(self.items))

shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
