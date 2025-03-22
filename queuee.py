class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

# Main code to interact with the user
def main():
    queue = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Size")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
            print(f"Enqueued: {item}")
        elif choice == 2:
            dequeued_item = queue.dequeue()
            if dequeued_item is None:
                print("Queue is empty, nothing to dequeue.")
            else:
                print(f"Dequeued: {dequeued_item}")
        elif choice == 3:
            peek_item = queue.peek()
            if peek_item is None:
                print("Queue is empty, nothing to peek.")
            else:
                print(f"Peek: {peek_item}")
        elif choice == 4:
            print(f"Queue size: {queue.size()}")
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
