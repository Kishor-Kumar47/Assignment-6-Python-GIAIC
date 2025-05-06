#  Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):                                        #Kishor Kumar
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price can't be negative!")
        else:
            print("Setting price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
item = Product(100)

print(item.price)    # Getting price
item.price = 150     # Setting price
print(item.price)    # Getting new price
del item.price       # Deleting price
