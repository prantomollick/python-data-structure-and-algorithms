"""
A singly linked list is a fundamental data structure consisting of a sequence of elements called nodes. Each node contains two parts: data and a reference (or pointers)
to the next node in the sequence. The first node is called the head, and the last node typically points to null, indicating the end of the list
1. Node structure
2. Dynamic size
3. Traversal
4. Insertion and deletion
5. Random Access
6. Memory Efficiency
7. Flexibility
8. Performance trade-offs



"""

class Node: 
    def __init__(self, data) -> None:
        """
        Represents a node in the singly linked list
        """
        self.data = data
        self.next = None
 

class LinkedList: 
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.insert_at_begin(data)
        else: 
            current_node = self.head
            position = 0
            while current_node and position + 1 != index:
                current_node = current_node.next
                position += 1
            
            if current_node:
                new_node.next = current_node.next
                current_node.next = new_node
    

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            

    def remove_node(self, data):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == data:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                
                break
            prev_node = current_node
            current_node = current_node.next
    
    def print_linked_list(self):
        current_node = self.head
        while current_node: 
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        
        print("None")
        
        






if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_begin(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_index(15, 1)
    linked_list.insert_at_end(25)
    linked_list.remove_node(20)
    linked_list.print_linked_list()

