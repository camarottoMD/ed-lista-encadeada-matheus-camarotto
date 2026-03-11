
#Cada nó da lista precisa tem seu valor e uma referencia para o próximo valor

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0 # atributo privado

    """
        Inserir elemento no ínicio da lista
    """
    def insert_beginning(self, value):
        if self.head:
            node = Node(value)
            aux = node.next
            
        else:
            self.head = value

    """
        Inserir elemento no final da lista
    """
    def insert_end(value):
        pass
    """
        remover um elemento da lista
    """
    def remove(value):
        pass
    """
        buscar um elemento da lista
    """
    def search(value):
        pass
    """
        imprimir os elementos na lista
    """
    def print_list():
        pass
    """
        retornar o tamanho da lista
    """
    def size():
        pass
    """
        verificar se a lista está vazia
    """
    def is_empty():
        pass

lista = LinkedList()
print(lista.insert_beginning(5))
print(lista.insert_beginning(3))