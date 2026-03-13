
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    def insert_end(self, value):
        node = Node(value)
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
        else:
            self.head = node
        self._size += 1

    def remove(self, index):
        if index < 0:
            raise IndexError("list index out of range")
        if not self.head:
            raise IndexError("empty list")
        if index == 0:
            self.head = self.head.next
            self._size -= 1
            return
        pointer = self.head
        for i in range(index - 1):
            if pointer.next:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")

        target = pointer.next
        if target:
            pointer.next = target.next
        else:
            raise IndexError("list index out of range")
        self._size -= 1

    def search(self, index):
        if index < 0:
            raise IndexError("list out of the range")
        if not self.head:
            raise IndexError("empty list")
        pointer = self.head
        for _ in range(index):
            if pointer.next:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer.data

    def print_list(self):
        if not self.head:
            raise IndexError("empty list")
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next

    def size(self):
        return self._size

    def is_empty(self):
        return self.head is None

if __name__ == "__main__":
    lista = LinkedList()
    lista.insert_beginning(5)
    lista.insert_beginning(3)
    lista.insert_end(9)
    lista.print_list()
    print(f'Size: {lista.size()}')
    lista.remove(2)
    lista.print_list()
    print(f'Size: {lista.size()}')