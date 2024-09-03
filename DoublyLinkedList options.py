class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Doubly_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def create(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
    def insert_at_front(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_at_position(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)
        pos = int(input("Enter the position: "))
        if pos == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:  # if the list was empty
                self.tail = new_node
            return
        current = self.head
        i = 0
        while i < pos - 1 and current.next is not None:
            current = current.next
            i += 1
        new_node.next = current.next
        new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        if new_node.next is None:  # if inserted at the end
            self.tail = new_node
    def insert_at_end(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def delete_front(self):
        if self.head is None:
            print("The list is empty.")
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            if self.head is None:  # if the list is now empty
                self.tail = None
    def delete_end(self):
        if self.head is None:
            print("The list is empty.")
        elif self.head.next is None:  # if there's only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    def delete_position(self):
        pos = int(input("Enter the position to delete: "))
        if self.head is None:
            print("The list is empty.")
        elif pos == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            i = 0
            while i < pos and current is not None:
                current = current.next
                i += 1
            if current is None:
                print("Position out of bounds.")
            else:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                if current == self.tail:  # if deleted node was the last node
                    self.tail = current.prev
obj = Doubly_LinkedList()
while True:
    print("""\nEnter 1.create
2.display
3.insert_at_front
4.insert_at_position
5.insert_at_end
6.delete_front
7.delete_end
8.delete_position
9.exit\n""")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        obj.create()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.insert_at_front()
    elif choice == 4:
        obj.insert_at_position()
    elif choice == 5:
        obj.insert_at_end()
    elif choice == 6:
        obj.delete_front()
    elif choice == 7:
        obj.delete_end()
    elif choice == 8:
        obj.delete_position()
    elif choice == 9:
        break
    else:
        print("Invalid choice")