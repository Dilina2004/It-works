class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

def main():
    name = input("Enter Employee Name: ")
    age = input("Enter Employee Age: ")
    department = input("Enter Employee Department: ")

    employee = Employee(name, age, department)
    employee.display_employee_info()