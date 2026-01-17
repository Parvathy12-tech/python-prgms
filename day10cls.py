from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, year_joined):
        self.name = name
        self.year_joined = year_joined

    def years_on_platform(self):
        current_year = 2025
        return current_year - self.year_joined

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.role()}) has been using the platform for {self.years_on_platform()} years."


class Customer(User):
    def role(self):
        return "Customer"


class Vendor(User):
    def role(self):
        return "Vendor"


# Example usage
users = [
    Customer("Alice", 2020),
    Vendor("Bob", 2018),
    Customer("Charlie", 2023)
]

for user in users:
    print(user)