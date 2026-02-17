class Bank:
    def __init__(self):
        self.balance = 0
        self.account = 0
        
    def account(self,acc_no):
        self.account = acc_no
        return acc_no

    def deposit(self,depo_amount):
        self.balance += depo_amount
        depo_amount = int(input("Enter the amount you want to deposit: "))
        bank.deposit(depo_amount)
        
    def balance(self):
        print("Current Balance:", self.balance)
        
    def withdrawl(self,withdraw):
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if self.balance > 0:
            final_balance = self.balance - withdraw
            print(final_balance)
        else:
            print("Not sufficient balance to withdraw the amount")
    
    def display(self):
       print("Account No:", self.account)
       print("Balance:", self.balance)
    
    def menu(self):
        print("1. account")
        print("2. deposit")
        print("3. balance")
        print("4. withdrawl")
        print("5. Display")
        print("6. Exit")
        
bank = Bank()

while True:
    bank.menu()
    choice = int(input('enter your choice: '))
    if choice == 1:
        acc_no = int(input("Enter your Account no: "))
        print(bank.account)
        
    elif choice == 2:
        depo_amount = int(input("Enter the amount you want to deposit: "))
        print(bank.deposit)
        
    elif choice == 3:
        print(bank.balance)
        
    elif choice == 4:
        print(bank.withdrawl)
        
    elif choice == 5:
        print(bank.display)
        
    elif choice == 6:
        break
    
    else:
        print("Invalid Input")

        
        
        
        
    
   

    
    
            
        
        