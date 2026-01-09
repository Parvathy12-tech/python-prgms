
class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):

        return self._balance + other._balance

    def display_details(self):
        return f"Account Holder: {self._name}, Balance: {self._balance}"

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05   



class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02   

savings = SavingsAccount("Ravi", 10000.0)
current = CurrentAccount("Anjali", 15000.0)


print(savings.display_details())
print("Interest (Savings):", savings.calculate_interest())

print(current.display_details())
print("Interest (Current):", current.calculate_interest())
total_balance = savings + current
print("Total Balance (Ravi + Anjali):", total_balance)