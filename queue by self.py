queue = []

def insert():
    item = input("Enter the value you want to enter: ")
    queue.append(item)
    
def deletion():
    if len(queue) == 0:
        print("underflow")
    else:
        deleted = queue.pop(0)
        print(deleted)

def traversal():
    if len(queue) == 0:
        print("underflow")
    else:
        print("Traversal on queue will be:")
        
        for i in queue:
            print(i)
            
while True:
    print("\nQueue Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Traversal")
    print("4. Exit")
    
    choice = int(input("Enter your choice here: "))
    
    if choice == 1:
        insert()
        
    elif choice == 2:
        deletion()
        
    elif choice == 3:
        traversal()
        
    elif choice == 4:
        break
    
    else:
        print("Invalid input")