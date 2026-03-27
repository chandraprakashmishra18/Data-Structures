<<<<<<< HEAD
class StackADT:
    def __init__(self):
        self.list = []
        
    def push(self , x):
        self.list.append(x)
        
    def pop(self):
        if len(self.list) == 0:
            return "Underflow"
        else:
            return self.list.pop()
    
    def peek(self):
        if len(self.list) == 0:
            return "Underflow"
        else:
            return self.list[-1]
        
    def isEmpty(self):
        if len(self.list) == 0:
            return "True"
        else:
            return "False"
        
    def size(self):
        return len(self.list)
    
    def display(self):
        if len(self.list) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", self.list)
    
def menu():
    st = StackADT()
    
    while True:
    
        print("\n--- STACK ADT MENU ---")

        # printing menu options
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Size")
        print("6. Display Stack")
        print("7. Reverse a String (Meaningful Use)")
        print("0. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            val = input("Enter your value : ")
            st.push(val)
            
        elif choice == 2:
            removed = st.pop()
            print(removed)
            
        elif choice == 3:
            top = st.peek()
            print(top)
            
        elif choice == 4:
            empty = st.isEmpty()
            print(empty)
            
        elif choice == 5:
            print(st.size())
            
        elif choice == 6:
            st.display()
            
        elif choice == 0:
            print("Thank you ")
            break 
        
        else:
            print("You entered an invalid input")
            
menu()
            
=======
class StackADT:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            print("pop from empty stack")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            print("peek from empty stack")
        return self.items[-1]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def display(self):
        return self.items[::-1]
    def search(self, item):
>>>>>>> ed2f51ce4940f185166ddd19bbe02f7be81f4ba2
