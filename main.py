
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def display_details(self):
        print(f"--- Employee Details ---")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")

class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, department, basic_salary, bonus):
        super().__init__(emp_id, name, department)
        self.basic_salary = basic_salary
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.basic_salary + self.bonus
    
    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self.basic_salary:.2f}")
        print(f"Bonus: ${self.bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, department, hourly_rate, hours_worked):
        super().__init__(emp_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self.hourly_rate:.2f}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class Intern(Employee):
    def __init__(self, emp_id, name, department, stipend):
        super().__init__(emp_id, name, department)
        self.stipend = stipend
    
    def calculate_salary(self):
        return self.stipend
    
    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self.stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

print("Welcome to Employee Management System")
print("Available Options:")
print("1️. Add Permanent Employee")
print("2️. Add Contract Employee")
print("3️. Add Intern")
print("4️. View All Employees")

employees = []

while True:
    choice = input("Select an option (or 'exit' to quit): ")
    if choice.lower() == 'exit':
        break
    elif choice == '1':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        basic_salary = float(input("Enter Basic Salary: "))
        bonus = float(input("Enter Bonus: "))
        employees.append(PermanentEmployee(emp_id, name, department, basic_salary, bonus))
    elif choice == '2':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        hourly_rate = float(input("Enter Hourly Rate: "))
        hours_worked = int(input("Enter Hours Worked: "))
        employees.append(ContractEmployee(emp_id, name, department, hourly_rate, hours_worked))
    elif choice == '3':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        stipend = float(input("Enter Stipend: "))
        employees.append(Intern(emp_id, name, department, stipend))
    elif choice == '4':
        print("\nAll Employees:\n")
        for emp in employees:
            emp.display_details()
    else:
        print("❌ Invalid option, please try again!\n")
