#  Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.



class A:
    def show(self):                                        #Kishor Kumar
        print("Class A → show()")

class B(A):
    def show(self):
        print("Class B → show()")

class C(A):
    def show(self):
        print("Class C → show()")

class D(B, C):  # Diamond inheritance
    pass

# Create an object of class D
obj = D()

# Call show() and observe MRO
obj.show()

# Print MRO to understand the method lookup path
print("Method Resolution Order (MRO):")
print(D.__mro__)
