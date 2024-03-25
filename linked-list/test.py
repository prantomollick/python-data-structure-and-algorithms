class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    """Imagine head has already node value 2 -> (hold on head) Now, we get new data to include as head of linked list, create new Node 1 -> newNode next pointer point 
    to -> 2(still head) -> after that change head value 1(head) -> 2 ->
    """
    def inser_at_begin(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
            
        
        

print(Node(2))