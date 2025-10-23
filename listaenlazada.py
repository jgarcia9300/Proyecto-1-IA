class Node:
    def __init__(self, valor):
        self.valor = valor
        self._siguiente = None # Python's version of "null" is "None"
        self._previo = None
 
class DobleListaEnlazada:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._N = 0
     
    def add_first(self, valor):
        """
        Parametros
        ----------
        valor: cualquiera
            Agrega un nuevo nodo al principio
        """
        nuevo_nodo = Node(valor)
        if not self._cabeza:
            # Si no hay nada en un inicio el nuevo elemento es tanto la cabeza
            # como la cola
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            nuevo_nodo._siguiente = self._cabeza
            self._cabeza._previo = nuevo_nodo
            self._cabeza = nuevo_nodo
        self._N += 1
     
    def add_last(self, valor):
        nuevo_nodo = Node(valor)
        if not self._cola:
          # Si no hay nada en un inicio el nuevo elemento es tanto la cabeza
          # como la cola
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            nuevo_nodo._previo = self._cola
            self._cola._siguiente = nuevo_nodo
            self._cola = nuevo_nodo
        self._N += 1
     
    def remove_first(self):
        """
        Remueve y retorna el primer valor de la lista enlazada
        o no hace nada y retorna None si la lista esta vacia
        """
        ret = None
        if self._cabeza: # If the head is not None
            ret = self._cabeza.valor
            if self._cabeza is self._cola:
                self._cabeza = None
                self._cola = None
            else:
                self._cabeza = self._cabeza._siguiente
                self._cabeza._previo = None
            self._N -= 1
        return ret

    def remove_last(self):
        """
        Remueve y retorna el ultimo valor de la lista enlazada
        o no hace nada y retorna None si ya esta vacia
       
        """
        ret = None
        if self._cola: # Si la cabeza es None
            ret = self._cola.valor
            if self._cabeza is self._cola:
                self._cabeza = None
                self._cola = None
            else:
                self._cola = self._cola._previo
                self._cola._siguiente = None
            self._N -= 1
        return ret
         
    def __str__(self):
        # metodo string
        s = "DobleListaEnlazada: "
        nodo = self._cabeza
        while nodo: #mientrad el nodo no sea None
            s += "{} ==> ".format(nodo.valor)
            nodo = nodo._siguiente
        return s
     
    def __len__(self):
        # Permite usar len() en los objetos para saber su longitud
        return self._N

if __name__ == '__main__':
    L = DobleListaEnlazada()
    L.add_first(10)
    L.add_first(4)
    L.add_first("chris")
    L.add_last("layla")
    L.add_last("theo")
    print(L)
    print(len(L))
    print(L.remove_first())
    print(L.remove_last())
    print(L)
    print(len(L))
