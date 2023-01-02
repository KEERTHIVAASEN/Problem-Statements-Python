# Define a class for linked list nodes
class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Create some nodes and link them together to form a linked list
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node1.next = node2
node2.next = node3

# Print the linked list
def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next

print_linked_list(node1)

# This program defines a simple LinkedListNode class that has a value and a reference to the next node in the list. It then creates three nodes and links them together to form a linked list, and prints the linked list using a loop.