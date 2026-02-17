
class stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self, x):
        self.items.append(x)
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items.pop()
    
    def peek(self):
        if not self.is__empty():
            return self.items[-1]
        else:
            return "stack is empty"
        
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
    
    def menu(self):
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Exit")
items=stack()
items.menu() 
choice = int(input("Enter your choice: "))
while True:
 if choice == 1:
                x = int(input("enter value to push: "))
                items.push(x)
                print("pushed", x)
 elif choice == 2:
                print("popped value:", items.pop())
 elif choice == 3:
                print("top value:", items.peek())
 elif choice == 4:
                print("size of stack:", items.size())
 elif choice == 5:
                print("stack elements:", items.display())
 else:
                print("invalid choice")
               
                
            
                
            
            
            
