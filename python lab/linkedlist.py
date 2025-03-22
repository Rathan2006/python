class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head
        prev = None
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print("Node with data", key, "not found.")
            return
        prev.next = current.next
        current = None

if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Delete node")
        print("4. Display linked list")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to insert at beginning: "))
            ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at end: "))
            ll.insert_at_end(data)
        elif choice == 3:
            key = int(input("Enter data of node to delete: "))
            ll.delete_node(key)
        elif choice == 4:
            ll.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
