class Node:
    def __init__(self ,data):
        self.data = data
        self .next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
                
            curr.next = new_node
            
    def traversal(self):
        curr = self.head
        while curr
            