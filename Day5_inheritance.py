class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__balance = 10000  
        print(f"{self.name} nu account thurannu")
        
    def show_balance(self):
        print(f"{self.name} nte balance: ₹{self.__balance}")

class Fresher(BankAccount):  
    def __init__(self, name, college):
        super().__init__(name)  
        self.college = college
        self.japan_dream = "¥440k"
        print(f"{college} il ninnu fresher aayi")
    
    def introduce(self):
        print(f"Njan {self.name}. Dream: {self.japan_dream}. Tokyo here I come!")

print("=== Day 5 Inheritance Test ===")
ramla = Fresher("Ramla", "Diploma College")
ramla.introduce()      
ramla.show_balance()
