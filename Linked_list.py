class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

class Linked_list:
    def __init__(self):
        self.head = None

    def len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def insert_at(self, data, index):
        if index < 0 or index >= self.len():
            raise Exception("Invalid index!")
        if index == 0:
            self.insert_at_beginning(data)
            return
        node = Node(data)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node.next = itr.next
                itr.next = node
                break
            count += 1
            itr = itr.next

    def remove_at(self, index):
        count = 0
        if index < 0 or index >= self.len():
            raise Exception("Invalid index!")
        if index == 0:
            self.head = self.head.next
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def remove_value(self, data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next
            return
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            raise Exception("Value is not on the list!")
            itr = itr.next

    def insert_values(self, list=[]):
        for element in list:
            self.insert_at_end(element)
        return

    def reverse(self, node):
        if node.next is None:
            self.head = node
            return
        self.reverse(node.next)
        temp_node = node.next
        node.next = temp_node.next
        temp_node.next = node

    def reverse_print(self, node):
        if node is None:
            return
        self.reverse_print(node.next)
        print(str(node.data) + " --> ", end="")

    def print_list(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        itr = self.head
        string = ''
        while itr:
            string += (str(itr.data) + " --> ")
            itr = itr.next
        print(string)

#sample input
my_ll = Linked_list()
my_ll.insert_at_beginning(19)
my_ll.insert_at_beginning(20)
my_ll.insert_at_end(18)
my_ll.insert_at_end(17)