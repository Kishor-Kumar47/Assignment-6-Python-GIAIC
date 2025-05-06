# Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


# Employee class (independent)
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"👤 Employee: {self.name}, ID: {self.emp_id}")

# Department class (aggregates Employee)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Reference to Employee object

    def show_department_details(self):
        print(f"🏢 Department: {self.dept_name}")
        self.employee.display_info()  # Access employee details

# Create an Employee object (independent)
emp1 = Employee("Alice", 101)

# Pass the existing Employee object to the Department
dept = Department("HR", emp1)

# Show department and employee info                      #Kishor Kumar
dept.show_department_details()
