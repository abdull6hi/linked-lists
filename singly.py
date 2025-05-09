class Node:
    def __init__(self, data):
        self.data = data      # Store the data
        self.next = None      # Pointer to the next node
class LinkedList:
    def __init__(self):
        self.head = None  

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
# Create a linked list
ll = LinkedList()

# Insert some elements
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

# Display the list
ll.display()
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head  # Point to old head
    self.head = new_node       # New node becomes head
def delete_node(self, key):
    current = self.head

    # If head is the node to delete
    if current and current.data == key:
        self.head = current.next
        current = None
        return

    # Search for node
    prev = None
    while current and current.data != key:
        prev = current
        current = current.next

    # If not found
    if current is None:
        print(f"{key} not found in list.")
        return

    # Unlink the node
    prev.next = current.next
    current = None
def search(self, key):
    current = self.head
    while current:
        if current.data == key:
            print(f"{key} found in list.")
            return True
        current = current.next
    print(f"{key} not found.")
    return False
def reverse(self):
    prev = None
    current = self.head

    while current:
        next_node = current.next  # Save next node
        current.next = prev       # Reverse the pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    self.head = prev
