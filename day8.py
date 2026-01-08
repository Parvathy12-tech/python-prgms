
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")


class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours
    
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name
    
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, "
              f"Working Hours: {self.working_hours}, Project: {self.project_name}")



p = Person("Alice", 30)
e = Employee("Bob", 40, "E123")
pt = PartTime("Charlie", 25, 20.5)
c = Consultant("Diana", 35, "C456", 15.0, "AI Project")


p.show_details()
e.show_details()
pt.show_details()
c.show_details()