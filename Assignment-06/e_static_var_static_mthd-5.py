# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a , b):
        return(a + b)                             #Kishor Kumar

result = MathUtils.add(40, 60)
print(f"The sum of 2 numbers is : {result}") #we can use f string also    
print("The sum of 2 numbers is :", result)    
