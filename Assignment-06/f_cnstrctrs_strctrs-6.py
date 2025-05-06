# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object has been created.")  # Constructor message

    def __del__(self):
        print("Logger object has been destroyed.")  # Destructor message

# Example usage
logger1 = Logger()                               #Kishor Kumar

# Deleting the object manually (optional)
del logger1
