from listaenlazada import DobleListaEnlazada

class Estado:
    def __init__(self, casillas):
        """
        Parametros
        ----------
        casillas : Lista 2D
            Lista de listas de casillas. Todas las casillas son numeros a expecion del blanco que es " " 
            Ejemplo: [[2, 6, 1], [7, " ", 3], [5, 8, 4]]
        """
        self.casillas = casillas
        self.prev = None

    def __repr__(self):
        """
        Retorna
        -------
        str
            Printable string del tablero
        """
        s = ""
        for i in range(len(self.casillas)):
            for j in range(len(self.casillas[i])):
                s += "{} ".format(self.casillas[i][j])
            s += "\n"
        return s
      
    def __eq__(self, other):
      return str(self) == str(other) 
    
    def __hash__(self):
       return hash(tuple([tuple(x) for x in self.casillas]))

    def __lt__(self, other):
        """
        Sobrecarga el operador menor que  para que los empates se
        resuelvan automaticamente en una estructura monton (heap) sin que
        el programa se bloquee
        Parametros
        ----------
        Otro : Estado

        Retorna
        -------
        bool
            Resultado de la comparacion entre strings (<)
        """
        return str(self) < str(other)

    def copy(self):
        """
        Retorna una copia profunda de este estado
        """
        casillas = []
        for i in range(len(self.casillas)):
            casillas.append([])
            for j in range(len(self.casillas[i])):
                casillas[i].append(self.casillas[i][j])
        return Estado(casillas)

    def is_goal(self):
        """
        Retorna
        -------
        bool
            Verdadero si es el estado objetivo, de lo contrario retorna falso
        """
        res = True
        N = len(self.casillas)
        contador = 1
        for i in range(N):
          for j in range(N):
            if i != N-1 or j != N-1:
                if self.casillas[i][j] != contador:
                    res = False
            contador += 1
        return res

    def get_neighbs(self):
        """
        Retorna
        -------
        lista de estados
            Una lista de los estados de los vecinos
        """
        N=len(self.casillas)
        neighbs = []
      
        ## Paso 1: Encontrar la fila y la columna de la casilla que esta en blanco
        fila = 0
        columna = 0
        for i in range (N):
            for j in range(N):
                if self.casillas[i][j] == " ":
                    fila = i
                    columna = j
        # Paso 2: Intercambia este indice con el vecino que pueda intercambiar
        
        for [i, j] in [[fila-1, columna], [fila+1, columna], [fila, columna-1], [fila, columna+1]]:
   
          if i>= 0 and j>= 0 and i < N and j < N:
              n = self.copy()
              ## Intercambio(fila, columna) con(i, j)
              n.casillas[fila][columna], n.casillas [i][j] = n.casillas[i][j], n.casillas[fila][columna]
              neighbs.append(n)
              

  
        return neighbs
      

    def solve(self):
        """
        Encuentra el camino más corto desde este estado al estado objetivo.
        """

        finalizado = False

        # Cola de estados descubiertos pero no explorados
        cola_estados = DobleListaEnlazada()
        cola_estados.add_last(self)

        limite_frontera = set([self])
        visitado = set([])

        estado_actual = None
        while not finalizado and len(cola_estados) > 0:
            print(len(cola_estados))
            estado_actual = cola_estados.remove_first()
            visitado.add(estado_actual)
            limite_frontera.remove(estado_actual)

            if estado_actual.is_goal():
                finalizado = True
            else:
                for vecino in estado_actual.get_neighbs():
                    if vecino not in limite_frontera and vecino not in visitado:
                        limite_frontera.add(vecino)
                        vecino.prev = estado_actual
                        cola_estados.add_last(vecino)

        # Reconstruir el camino de solución
        solucion = [estado_actual]
        while estado_actual.prev:
            estado_actual = estado_actual.prev
            solucion.append(estado_actual)
        solucion.reverse()
        return solucion



# Ejemplo
estado1 = Estado([[5, 6, 8], [" ", 4, 7], [1, 3, 2]])
solucion = estado1.solve()
for x in solucion:
    print(x, end="\n\n")