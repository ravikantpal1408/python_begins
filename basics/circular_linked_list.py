class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    # Declaring head and tail pointer as null.
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    # This function will add the new node at the end of the list.
    def add(self, data):
        newNode = Node(data)
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # tail will point to new node.
            self.tail.next = newNode
            # New node will become new tail.
            self.tail = newNode
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head

    # Deletes node from the beginning of the list
    def delete_node(self, deletekey):
        current_node = self.head
        prev_node = None
        while current_node:

            # The node to be deleted is the head node
            if current_node.data == deletekey and current_node == self.head:

                # Case 1 - The head is the only element in circular linked list
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return

                # Case 2 - There are more elements in the circular linked list
                else:
                    # Traverse to end of list, update self.head, delete head
                    while current_node.next != self.head:
                        current_node = current_node.next

                    current_node.next = self.head.next
                    self.head = self.head.next
                    current_node = None
                    return

            # Case 3 & 4 - Node to be deleted in between nodes or last node
            elif current_node.data == deletekey:
                prev_node.next = current_node.next
                current_node = None
                return

            else:
                if current_node.next == self.head:
                    break

            prev_node = current_node
            current_node = current_node.next

            pass
        pass

    # Displays all the nodes in the list
    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            # Prints each node by incrementing pointer.
            print(current.data, end=' ')
            while current.next != self.head:
                current = current.next;
                print(current.data, end=' ')
            print("\n")

    # Searches for a node in the list
    def search(self, element):
        current = self.head
        i = 1
        flag = False
        # Checks whether list is empty
        if self.head is None:
            print("List is empty 👀")
        else:
            while True:
                # Compares element to be found with each node present in the list
                if current.data == element:
                    flag = True
                    break
                current = current.next
                i = i + 1
                if current == self.head:
                    break
            if flag:
                print("Element is present in the list at the position : 😃 \n" + str(i))
            else:
                print("Element is not present in the list 📭 \n")


_obj = CircularLinkedList()

if __name__ == "__main__":

    while True:
        choice = int(input("Enter your choice 👩🏻‍🎤 \n"))
        if choice == 1:
            input_value = input("Enter a value to add  🧙🏻 \n")
            _obj.add(input_value)
            print("Item added !! 🧑🏻‍💻")

        if choice == 2:
            input_value = input("Enter item to be searched 👩🏻‍🦯 \n")
            _obj.search(input_value)
            pass

        if choice == 3:
            input_value = input("Enter item to be deleted ❌ \n")
            _obj.delete_node(input_value)
            pass

        if choice == 4:
            print('Displaying all content of circular linked list 🤖 \n')
            _obj.display()
            pass

        if choice == 5:
            print("Ok done ... Bye !! 💃🏻 \n")
            break
