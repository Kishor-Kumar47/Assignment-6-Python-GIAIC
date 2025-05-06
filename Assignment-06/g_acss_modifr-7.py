



class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


    def get_ssn(self):                             #Kishor Kumar
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("salary must be positive in number")

    def display(self):
        print(f"Name: {self.name}") #public           
        print(f"Salary: {self._salary} ")# protected           
        print(f"SSN: {self.__ssn}") # private           

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")    
        print(f"Department: {self.department}")    
        print(f"Protected Salary: {self._salary}")    
        print(f"Accessing SSN via getter command: {self.get_ssn()}")   #private veriable 

m = Manager("Kishor", "34000", "93837", "Social Science")
m.show_manager_info()
m.set_salary(64000)
print("Update Salary:", m._salary)

# print(m.__ssn)
print("Private SSN via managed: ", m._Employee__ssn )