# Engine class
class Engine:
    def start(self):
        print("🔧 Engine started.")

# Car class that uses composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        print("🚗 Car is starting...")
        self.engine.start()  # Access Engine's method via Car

# Example usage
my_engine = Engine()                               #Kishor Kumar
my_car = Car(my_engine)

my_car.start_car()
