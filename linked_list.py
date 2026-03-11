
#Cada nó da lista precisa tem seu valor e uma referencia para o próximo valor

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None #ISSO E O PONTEIRO 


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
            node.next = self.head
            self.head = node
            self._size += 1

    """
        Inserir elemento no final da lista
    """
    def insert_end(self, value):
        if self.head:
            pointer = self.head #vai criar a "lanterna"
            while(pointer.next): 
                """laco ate o pointer valer None,  
                Enquanto o nó atual tiver um próximo (next), passe para o próximo, 
                primeira parte vai fazer ele correr todos os pointer, e a segunda vai atribuir o valor do proximo no no pointer, ate chegar a none"""
                pointer = pointer.next
            pointer.next = Node(value) # chego no ultimo no, e avanco mais um, adicionando agora um outro no na ultima posicao
        else:
            self.head = value
        self._size = self._size + 1

    """
        remover um elemento da lista
    """
    def remove(self, value):
        

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