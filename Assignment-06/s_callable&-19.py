# callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an instance
times_three = Multiplier(3)

# Check if the object is callable
print(callable(times_three))  # ✅ Output: True

# Call the object like a function                           #Kishor Kumar
result = times_three(10)
print("Result:", result)  # ✅ Output: 30
