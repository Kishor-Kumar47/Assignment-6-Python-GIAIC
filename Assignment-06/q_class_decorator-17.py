# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply decorator to Person class
@add_greeting
class Person:                                              #Kishor Kumar
    def __init__(self, name):
        self.name = name

# Create object and call the added method
p = Person("Alice")
print(p.greet())  # Output: Hello from Decorator!
