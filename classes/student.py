class Student:
    school_value ="Python High School"

    def __init__(self, name):
        self.name = name
        self.__grades = []

    def add_grades(self, grade):
        if isinstance(grade, int) and 0 <= grade <=100:
            self.__grades.append(grade)
        else:
            print("Invalid grade Must be an integer between 0 and 100")


    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)
    

    def has_passed(self):
        return self.average() >=50
    

alice = Student("Alice")
alice.add_grades(85)
alice.add_grades(70)
alice.add_grades(90)

print(f"Average grade: {alice.average()}")
print(f"Has passed: {alice.has_passed()}")