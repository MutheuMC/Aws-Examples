class Employee:
    employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


        Employee.employees.append(self.name)


    def get_details(self):
            return f"Employee : {self.name}  , Salary: {self.salary}"
            
class Manager(Employee):

    def __init__(self,name, salary, department):
        super().__init__( name, salary)
        self.department = department


    def get_details(self):
            return f"Manager : {self.name}  , Salary: {self.salary}, Department : {self.department}"
    

alice = Employee('Alice', 50000)
alice1 = Employee('Alicia', 50000)


bob = Manager('Bob', 80000, "IT")


print(bob.get_details())

print(Employee.employees)