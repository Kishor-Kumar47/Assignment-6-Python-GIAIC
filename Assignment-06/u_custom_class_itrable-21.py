# Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

# Once you are done submit this form ASAP:

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
                                                              #Kishor Kumar
    def __iter__(self):
        return self  # The iterator is the object itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration once countdown reaches 0
        self.current -= 1
        return self.current  # Return the current countdown value

# Example usage in a for-loop
countdown = Countdown(5)
for number in countdown:
    print(number)
