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
        Encuentra el camino mas corto desde este estado al estado objetivo

        Retorna
        -------
        lista de estados
             Un camino desde este estado al estado objetivo 
             donde el primer elemento es este estado y el ultimo el objetivo
    
        """

        finalizado = False

        #frontera: nodos descubiertos pero no explorados
        frontera = DobleListaEnlazada()
        frontera.add_last(self)
        
        limite_frontera = set ([self])
        visitado = set([])
        
        #Cada vertice pasa por la frontera solo una vez
        v = None
        while not finalizado and len(frontera) > 0: # 0(V) iteraciones
          print(len(frontera))
          v = frontera.remove_first() # 0(1)
          visitado.add(v)
          limite_frontera.remove(v)
          if v.is_goal():
            finalizado = True
          else:
             #revisa cada vecino de v
            for n in v.get_neighbs():
              if n  not in limite_frontera and n not in visitado:
                """
                Cambia el estado del nodo para indicar que se agrega
                al final de la frontera
                
                """
                limite_frontera.add(n)
                n.prev = v
                frontera.add_last(n)
   

  
        # TODO: Para realizar

        solucion = [v]
        while v.prev:
          v = v.prev
          solucion.append(v)
        solucion.reverse()
        return solucion


# Ejemplo
estado1 = Estado([[5, 6, 8], [" ", 4, 7], [1, 3, 2]])
solucion = estado1.solve()
for x in solucion:
    print(x, end="\n\n")