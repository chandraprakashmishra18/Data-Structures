class Bank:
    def __int__(self):
        self.account = 0
        self.balance = 0
        
    def acc(self , x):
        x = int(input("Enter your acc no : "))
        x = self.account
        
    def deposit(self , depo):
        depo = int(input("Enter the amount you want to deposit: "))
        self.balance =+ depo
        return(self.balance)
    
    def bal(self):
        return(self.balance)
    
    def withdrawl(self):
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw >= self.balance:
            self.balance-withdraw = self.balance
            return(self.balance)
        else:
            print("Not sufficient amount")
            
    def display(self):
        print(self.account)
        print(self.balance)
        
    def menu(self):
        print("1. account")
        print("2. deposit")
        print("3. balance")
        print("4. withdrawl")
        print("5. Display")
        print("6. Exit")
        
bank = Bank()
bank.menu()

choice = int(input("Enter your choice: "))
if choice == 1:
    print(bank.acc)
    

    
          
        
    