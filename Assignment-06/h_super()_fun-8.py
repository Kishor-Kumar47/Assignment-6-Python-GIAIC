class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)                        #Kishor Kumar
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

t= Teacher("Kishor", "Python")