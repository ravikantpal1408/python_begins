class Node:
    def __init__(self, data):
        self.data = data
        self.n_ref = None  # next reference
        self.p_ref = None  # previous reference


class DoubleLinkedList:
    def __init__(self):
        self.start_node = None

    def add_item(self, data):
        if self.start_node is None:
            # node is empty
            new_node = Node(data)
            self.start_node = new_node
            print("Item inserted !! 👨🏻‍🌾 \n")
            return
        else:
            print("Node is not empty 🤖 \n")
            pass
        pass

    def insert_at_start(self, data):
        if self.start_node is Node:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted !!")
            return

        new_node = Node(data)
        new_node.n_ref = self.start_node
        self.start_node.p_ref = new_node
        self.start_node = new_node
        pass

    def insert_at_enc(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.n_ref is not None:
            n = n.n_ref
        new_node = Node(data)
        n.n_ref = new_node
        new_node.p_ref = n
        pass

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.n_ref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.p_ref = n
                new_node.n_ref = n.n_ref
                if n.n_ref is not None:
                    n.n_ref.prev = new_node
                n.n_ref = new_node
                pass
            pass
        pass

    def insert_before_item(self, x, data):

        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.n_ref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.n_ref = n
                new_node.p_ref = n.p_ref
                if n.p_ref is not None:
                    n.p_ref.n_ref = new_node
                n.p_ref = new_node
                pass
            pass
        pass


