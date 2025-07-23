class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2(self.width * self.height)
    

class  Student:
    student_count = 0

    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

        student_count += student_count

    def get_student_count(self):
        return Student.student_count
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi my name is {self.name} and I am {self.age} years old"
    

class Teacher(Person):

       def __init__(self, name, age, subject):
           super().__init__(name, age)
           self.subject = subject

       def introduce(self):
           return f"Hi my name is {self.name} and I ma {self.age} years old and i teach {self.subject}"


class BankAccount:

    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return f"You have successfully withdrawn {amount} and yout current balance {self.__balance}"
        
    
bob = BankAccount()
bob.deposit(5999)
bob.withdraw(4000)
print(bob.balance)
    
class Polynomial:

    def __init__(self, coefficients=None):
        if coefficients is None:
         self.coefficients = []

        else:
            self.coefficients = coefficients

        

    def __str__(self):
        terms = []
        for power, coeff in enumerate(self.coefficients):
            if coeff == 0:
                continue
            elif power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
        return " + ".join(terms) if terms else "0"
    
    def __add__(self, other):
        # Pad the shorter with zeros
        max_len = max(len(self.coefficients), len(other.coefficients))
        c1 = self.coefficients + [0] * (max_len - len(self.coefficients))
        c2 = other.coefficients + [0] * (max_len - len(other.coefficients))
        result = [a + b for a, b in zip(c1, c2)]
        return Polynomial(result)

    def __repr__(self):
        return f"Polynomial({self.coefficients})"




   


