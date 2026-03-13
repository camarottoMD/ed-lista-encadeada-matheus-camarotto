
#Cada nó da lista precisa tem seu valor e uma referencia para o próximo valor

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None #ISSO É O VALOR DO PROXIMO NÓ 

        """
        PONTEIRO É ALGO QUE VAI APENAS GUIAR E APONTAR PARA UM NÓ
        """

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0 # atributo privado

    """
        Inserir elemento no ínicio da lista
    """
    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    """
        Inserir elemento no final da lista
    """
    def insert_end(self, value):
        node = Node(value)
        if self.head:
            pointer = self.head #vai criar a "lanterna"
            while pointer.next: 
                # Avanca ate encontrar o ultimo no da lista.
                pointer = pointer.next
            pointer.next = node # chego no ultimo no, e avanco mais um, adicionando agora um outro no na ultima posicao
        else:
            self.head = node
        self._size += 1
    """
        remover um elemento da lista
    """
    def remove(self, index):
        if index < 0:
            raise IndexError("list index out of range")
        if not self.head: #se trata de uma exceção, não faz sentido puxar um if normal
            raise IndexError("empty list") 
        if index == 0:
            self.head = self.head.next
            self._size -= 1
            return #finaliza o programa caso o indice seja 0
        pointer = self.head
        for i in range(index - 1):
            if pointer.next: # isso vai evitar com que acesse um pointer == None, então verificamos sempre o proximo nó para não ter um erro
                pointer = pointer.next #esse pointer vamos precisar atribuir pro nó anterior ao que vamos remover
            else: 
                raise IndexError("list index out of range")
            
        target = pointer.next #atribui o valor de none para o próximo nó, o nó que quero remover, pois a lista vai "esquecer" esse valor. 'Garbage Collection'
        if target:
            pointer.next = target.next #acessa o valor do nó seguinte ao que estou(index - 1), e atribui o valor do nó que esta após ao nó que quero remover
        else:
            raise IndexError("list index out of range")
        self._size -= 1

        
    """
        buscar um elemento da lista
    """
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
        
    """
        imprimir os elementos na lista
    """
    def print_list(self):
        if not self.head:
            raise IndexError("empty list")
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next
    """
        retornar o tamanho da lista
    """
    def size(self):
        return self._size
    
    """
        verificar se a lista está vazia
    """
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