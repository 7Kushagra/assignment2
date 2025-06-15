#
# Part 1: The Node Class
#
class Node:
    """
    Represents a single node in a singly linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        """
        Initializes a new Node.
        
        Args:
            data: The value to be stored in the node.
        """
        self.data = data
        self.next = None  # The reference to the next node, initialized to None

#
# Part 2: The LinkedList Class
#
class LinkedList:
    """
    Manages the collection of nodes and provides methods for list operations.
    """
    def __init__(self):
        """
        Initializes an empty LinkedList.
        The head is the starting point of the list.
        """
        self.head = None

    def add_node(self, data):
        """
        Adds a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        
        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        
        # Attach the new node at the end
        current.next = new_node

    def print_list(self):
        """
        Prints the data of all nodes in the list in order.
        Example output: 10 -> 20 -> 30 -> None
        """
        if self.head is None:
            print("List is empty.")
            return

        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        
        print(" -> ".join(nodes) + " -> None")

    def delete_node(self, n):
        """
        Deletes the nth node from the list (1-based index).

        Args:
            n (int): The 1-based index of the node to delete.

        Raises:
            ValueError: If the list is empty or if the index is out of range.
        """
        # --- Exception Handling: Deleting from an empty list ---
        if self.head is None:
            raise ValueError("Cannot delete from an empty list.")

        # Case 1: Deleting the head node (n=1)
        if n == 1:
            self.head = self.head.next
            return

        # Case 2: Deleting a node in the middle or at the end
        current = self.head
        previous = None
        count = 1

        # Traverse the list to find the nth node
        while current and count < n:
            previous = current
            current = current.next
            count += 1
            
        # --- Exception Handling: Index out of range ---
        # This occurs if we traverse past the end of the list
        if current is None:
            raise ValueError(f"Index {n} is out of range.")
        
        # Unlink the node from the list
        previous.next = current.next

#
# Part 3: Testing the Implementation
#
if __name__ == "__main__":
    
    # 1. Create a new linked list
    my_list = LinkedList()
    print("--- Initial Empty List ---")
    my_list.print_list()

    # 2. Add nodes to the list
    print("\n--- Adding Nodes (10, 20, 30, 40) ---")
    my_list.add_node(10)
    my_list.add_node(20)
    my_list.add_node(30)
    my_list.add_node(40)
    my_list.print_list()

    # 3. Delete nodes from the list
    print("\n--- Deleting Nodes ---")

    # Delete the head node (index 1)
    print("Deleting node at index 1 (value 10)...")
    my_list.delete_node(1)
    my_list.print_list()

    # Delete a middle node (index 2, which is now '30')
    print("\nDeleting node at index 2 (value 30)...")
    my_list.delete_node(2)
    my_list.print_list()
    
    # Delete the last remaining node (which is now at index 2)
    print("\nDeleting node at index 2 (value 40)...")
    my_list.delete_node(2)
    my_list.print_list()
    
    # 4. Test Exception Handling
    print("\n--- Testing Exception Handling ---")
    
    # Test deleting with an out-of-range index
    try:
        print("\nAttempting to delete node at index 5 (out of range)...")
        my_list.delete_node(5)
    except ValueError as e:
        print(f"Successfully caught expected error: {e}")
    my_list.print_list()

    # Clear the list to test deleting from an empty list
    print("\nDeleting the last node (index 1) to make the list empty...")
    my_list.delete_node(1)
    my_list.print_list()
    
    # Test deleting from an empty list
    try:
        print("\nAttempting to delete from an empty list...")
        my_list.delete_node(1)
    except ValueError as e:
        print(f"Successfully caught expected error: {e}")