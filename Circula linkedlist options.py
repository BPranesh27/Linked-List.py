class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Circular_Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def create(self):
        data = int(input("Enter the data: "))
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head  # Circular link
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head  # Circular link
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()
    def insert_at_front(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Circular link
    def insert_at_position(self):
        data = int(input("Enter the data: "))
        newnode = Node(data)
        pos = int(input("Enter the position: "))
        if pos == 0:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = self.head  # Circular link
            if self.tail is None:  # if the list was empty
                self.tail = newnode
            return
        current = self.head
        i = 0
        while i < pos-1 and current.next != self.head:
            current = current.next
            i += 1
        newnode.next = current.next
        current.next = newnode
        if newnode.next == self.head:  # if inserted at the end
            self.tail = newnode
    def insert_at_end(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link
    def delete_front(self):
        if self.head is None:
            print("The list is empty.")
        elif self.head == self.tail:  # If there's only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head  # Circular link
    def delete_end(self):
        if self.head is None:
            print("The list is empty.")
        elif self.head == self.tail:  # If there's only one node
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
    def delete_position(self):
        pos = int(input("Enter the position to delete: "))
        if self.head is None:
            print("The list is empty.")
        elif pos == 0:
            if self.head == self.tail:  # If there's only one node
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head  # Circular link
        else:
            current = self.head
            prev = None
            i = 0
            while i < pos and current.next != self.head:
                prev = current
                current = current.next
                i += 1
            if current == self.head:
                print("Position out of bounds.")
            else:
                prev.next = current.next
                if current == self.tail:  # If deleted node was the last node
                    self.tail = prev
                    self.tail.next = self.head  # Circular link
obj = Circular_Linkedlist()
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
