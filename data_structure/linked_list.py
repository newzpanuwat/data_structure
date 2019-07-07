class Node:
    """
    An object for storing a single node of a linked list
    """
    data = None
    next_node = None

    def __init__(self, data): 
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Return the number of nodes in the list
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds a new node contain a data at head
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node