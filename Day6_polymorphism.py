class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__balance = 10000
        
    def withdraw(self, amount):
        print(f"{self.name}: Standard withdrawal ₹{amount}")

class Fresher(BankAccount):
    def __init__(self, name, college):
        super().__init__(name)
        self.college = college
        self.japan_dream = "¥440k"
        
    def withdraw(self, amount):
        print(f"{self.name}: Fresher discount! Only ₹{amount-100} withdrawn")

class JapaneseWorker(BankAccount):
    def __init__(self, name):
        super().__init__(name)
        self.salary_yen = 440000
        
    def withdraw(self, amount):
        print(f"{self.name}: Salary withdrawal ¥{amount}. Tax deducted!")

def process_withdrawal(account, amount):
    account.withdraw(amount) 

print("=== Day 6 Polymorphism Test ===")
ramla_fresher = Fresher("Ramla", "Diploma College")
ramla_tokyo = JapaneseWorker("Ramla-San")

process_withdrawal(ramla_fresher, 500)   
process_withdrawal(ramla_tokyo, 100000)
