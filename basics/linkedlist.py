# Node
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # get data at that location
    def get_data(self):
        return self.data

    # get next element in the linked list
    def get_next(self):
        return self.next_node

    # point to the node specified by argument
    def set_next(self, new_next):
        self.next_node = new_next
        pass

    pass


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        pass

    # insert element in linked list
    def insert_el(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        pass

    # get size
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # search linked list
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                found = False
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")

        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError('Data not in the list')

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


linked_list = LinkedList()

while True:
    print('Enter your choice out of these provided options 👋🏻 \n')
    print(' 1- Insert item in linked options 👈\n',
          '2- see the size of linked list 🧩\n',
          '3- search item in a linked list 👀 \n',
          '4- delete item from linked list ⚔️\n')
    try:
        choice = int(input('Enter for choice 🖌 :\n'))

        if choice == 1:
            item = input('Enter item to insert into the linked list ◀️:\n')
            try:
                linked_list.insert_el(item)
                print('Item inserted in linked list 💫')
            except:
                print('Error inserting item 💥')

        if choice == 2:
            print('Size of linked list is 🚹 :- ', linked_list.size())
        if choice == 3:
            search_val = input('Enter item value to search into the linked list 🦸‍♂️ !! :\n')
            try:
                result = linked_list.search(search_val)
                print(f'Item [{search_val}] found at memory location - {result}👩🏻‍🚒 \n')
            except:
                print('Not found 📭')
        if choice == 4:
            delete_val = input('Enter item to be deleted ❌ :\n')
            try:
                linked_list.delete(delete_val)
                print('Item deleted successfully !! ✅\n')
            except:
                print('Item is not valid entry 🛑\n')
        if choice == 5:
            print('Thank you ! Now exiting !!🌐\n')
            break
            pass
    except:
        print('Invalid choice 🚫\n')


