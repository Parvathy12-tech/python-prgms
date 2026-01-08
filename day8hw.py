
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")



class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)   
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}")



class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)   
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")



class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)   
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, "
              f"Specialization: {self.specialization}, Yoga Style: {self.yoga_style}")



emp = Employee("Alice", "Receptionist")
trainer = Trainer("Bob", "Trainer", "Weight Training")
yoga_instructor = YogaInstructor("Clara", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("David", "MultiTrainer", "Cardio", "Vinyasa Yoga")


emp.display()
trainer.display()
yoga_instructor.display()
multi_trainer.display()