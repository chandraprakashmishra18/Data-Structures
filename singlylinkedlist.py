
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def traverse(self):
        temp = self.head
        if temp is None:
            print("Linked List is empty")
            return
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    def search(self, key):
        temp = self.head
        position = 1
        while temp is not None:
            if temp.data == key:
                print(f"Element {key} found at position {position}")
                return
            temp = temp.next
            position += 1
        print(f"Element {key} not found in linked list")
ll = LinkedList()
# Inserting elements
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

# Traversing linked list
print("Linked List elements:")
ll.traverse()

# Searching elements
ll.search(30)
ll.search(50)
            