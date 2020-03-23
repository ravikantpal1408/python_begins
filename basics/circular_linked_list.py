class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None)  # this is the sentinel node
        self.head.next = self.head  # link it to itself

    def add(self, data):  # no special case code is needed for an empty list
        self.head.next = Node(data, self.head.next)
        pass

    def __contains__(self, data):
        current = self.head.next
        while current != data:
            if current.data == data:  # element found
                return True
            current = current.next

        return False


_obj = CircularLinkedList()

while True:
    choice = int(input("Enter your choice 👩🏻‍🎤 \n"))
    if choice == 1:
        input_value = input("Enter a value to add  🧙🏻 \n")
        _obj.add(input_value)
        print("Item added !! 🧑🏻‍💻")

    if choice == 2:
        input_value = input("Enter item to be searched 👩🏻‍🦯 \n")
        search_result = _obj.__contains__(input_value)
        print(f'Item - {input_value} was found at {search_result}')
        pass

    if choice == 3:
        print("Ok done ... Bye !! 💃🏻 \n")
        break
