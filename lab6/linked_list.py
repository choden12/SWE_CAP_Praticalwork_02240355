class Node:
    def __init__(self, data):
        # Initialize the node with data and set the next pointer to None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

    def append(self, data):
        # Add a new node with the given data at the end of the list
        new_node = Node(data)
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        # Otherwise, traverse to the last node and append the new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        # Display the elements of the list in order
        elements = []
        current = self.head
        while current:
            elements.append(current.data)  # Collect data from each node
            current = current.next
        print(" -> ".join(map(str, elements)))  # Print data in linked format

    def insert(self, data, position):
        # Insert a new node with the given data at a specific position
        new_node = Node(data)
        if position == 0:
            # Insert at the head if position is 0
            new_node.next = self.head
            self.head = new_node
            return
        # Traverse to the position or end of the list
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")  # Raise an error if position is invalid
            current = current.next
        # Insert the new node at the desired position
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        # Delete the first node containing the given data
        if not self.head:
            return  # List is empty, nothing to delete
        if self.head.data == data:
            # If head contains the data, update head to the next node
            self.head = self.head.next
            return
        # Traverse to find the node to delete
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Remove the node
                return
            current = current.next

    def search(self, data):
        # Search for the data in the list and return its position
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position  # Return the position if found
            current = current.next
            position += 1
        return -1  # Return -1 if not found

    def reverse(self):
        # Reverse the linked list
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Temporarily store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev and current one step forward
            current = next_node
        self.head = prev  # Update head to the new front of the list

    # Exeercise 1

    def find_middle(self):
        # Find the middle element using slow and fast pointers
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
        return slow.data if slow else None  # Return data at slow pointer
    
    # Exercise 2

    def has_cycle(self):
        # Detect if the linked list contains a cycle using slow and fast pointers
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
            if slow == fast:
                return True  # If slow and fast meet, there is a cycle
        return False  # If no meeting point, no cycle
    
    # Exercise 3

    def remove_duplicates(self):
        # Remove duplicate values from the list
        seen = set()  # Track seen values
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                # If data is a duplicate, skip the current node
                prev.next = current.next
            else:
                # If data is unique, add it to seen and move prev forward
                seen.add(current.data)
                prev = current
            current = current.next  # Move to the next node

    # Exercise 4

    @staticmethod
    def merge_sorted(list1, list2):
        # Merge two sorted linked lists into one sorted linked list
        merged = LinkedList()
        p1 = list1.head  # Pointer for the first list
        p2 = list2.head  # Pointer for the second list

        # Traverse both lists, adding the smaller node to the merged list
        while p1 and p2:
            if p1.data < p2.data:
                merged.append(p1.data)
                p1 = p1.next
            else:
                merged.append(p2.data)
                p2 = p2.next

        # Append remaining nodes from either list (if any)
        while p1:
            merged.append(p1.data)
            p1 = p1.next
        while p2:
            merged.append(p2.data)
            p2 = p2.next

        return merged


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("Original List:")
ll.display() 

ll.insert(4, 1)
print("After Inserting 4 at position 1:")
ll.display()  

ll.delete(2)
print("After Deleting 2:")
ll.display()  

print("Position of 4:", ll.search(4)) 

ll.reverse()
print("Reversed List:")
ll.display()  

print("Middle element:", ll.find_middle()) 

ll2 = LinkedList()
ll2.append(2)
ll2.append(6)
merged_list = LinkedList.merge_sorted(ll, ll2)
print("Merged List:")
merged_list.display() 
