class Estado:
    def __init__(self, casillas):
        """
        Parametros
        ----------
        casillas : Lista 2D
            Lista de listas de casillas. Todas las casillas son umeros a expecion del blanco que es " " 
            Ejemplo: [[2, 6, 1], [7, " ", 3], [5, 8, 4]]
        """
        self.casillas = casillas
        self.prev = None

    def __repr__(self):
        """
        Returns
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

    def __lt__(self, other):
        """
        Overload the less-than operator so that ties can be broken
        automatically in a heap without crashing.
        Sobrecarga el operador menor que en para que los empates se
        resuelvan automaticamente en una estructura monton (heap) sin que
        el programa se bloquee
        Parametros
        ----------
        Otro : Estado
            Otro Estado

        Retorna
        -------
        bool
            Result of < comparison between string representations
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
              ## Swap(rol, col) with(i, j)
              n.casillas[fila][columna], n.casillas [i][j] = n.casillas[i][j], n.casillas[fila][columna]
              neighbs.append(n)
              

        print(fila, columna)
        return neighbs
      


    def solve(self):
        """
        Encuentra el camino mas corto desde este estado al estado objetivo

        Retorna
        -------
        lista de estados
             Un camino desde este estado al estado objetivo 
             donde el primer elemento es este estado y el ultimo el objetivo
    
        """
        vistado = {}
        cola = [self]
        finalizado = False
        # TODO: fill this in

        solucion = []
        return solucion


# Ejemplo
estado = Estado([[1, 2, 3], [4, 5, 6], [7, 8, " "]])
# state.get_neighbs()
# print(state)

for n in estado.get_neighbs():
    print(n, "\n\n")


objetivo = Estado([[1, 2, 3], [4, 5, 6], [7, 8, " "]])
print(objetivo.is_goal())