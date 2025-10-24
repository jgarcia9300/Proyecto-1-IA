import itertools
import heapq
import time

"""
 representacion de un nodo en el árbol de búsqueda A*
"""
class NodoRompecabezas:
    def __init__(self, estado_tablero, nodo_padre=None, movimiento=None):
        self.estado_tablero = estado_tablero          # estado actual del tablero
        self.nodo_padre = nodo_padre                  # nodo desde el cual se llego a este estado
        self.movimiento = movimiento                  # movimiento realizado para llegar aquí
        self.g = nodo_padre.g + 1 if nodo_padre else 0  # costo desde el estado inicial

    @property
    def h(self):
        """estimacion del coste restante (distancia Manhattan)"""
        return self.estado_tablero.manhattan

    @property
    def f(self):
        """funcion A*: f = g + h"""
        return self.g + self.h

    # metodos de comparación para usar en la cola de prioridad (heap)
    def __lt__(self, otro):
        return self.f < otro.f

    def __eq__(self, otro):
        return self.estado == otro.estado

    def __hash__(self):
        return hash(self.estado)

    @property
    def estado(self):
        """Representación del estado como tupla (para sets)"""
        return tuple(itertools.chain(*self.estado_tablero.tablero))

    @property
    def camino(self):
        """reconstruye el camino desde el nodo 
        inicial hasta este nodo"""
        nodo, ruta = self, []
        while nodo:
            ruta.append(nodo)
            nodo = nodo.nodo_padre
        return list(reversed(ruta))

    @property
    def resuelto(self):
        """indica si ya se llego al estado objetivo"""
        return self.estado_tablero.resuelto


"""
Uso de A* para resolver el puzzle
"""

class AlgoritmoAEstrella:
  
    def __init__(self, estado_inicial):
        self.estado_inicial = estado_inicial

    def resolver(self):
  
        frontera = []  # nodos por explorar (ordenados por f = g + h)
        heapq.heappush(frontera, (0, NodoRompecabezas(self.estado_inicial)))
        cerrada = set()  # estados ya explorados

        while frontera:
            _, nodo_actual = heapq.heappop(frontera)

            if nodo_actual.estado in cerrada:
                continue
            cerrada.add(nodo_actual.estado)

            if nodo_actual.resuelto:
                return nodo_actual.camino

            # movimientos válidos
            for funcion_movimiento, nombre_movimiento in nodo_actual.estado_tablero.movimientos_validos:
                nodo_hijo = NodoRompecabezas(funcion_movimiento(), nodo_actual, nombre_movimiento)
                if nodo_hijo.estado not in cerrada:
                    heapq.heappush(frontera, (nodo_hijo.f, nodo_hijo))

        return None  # en caso de no hallar solucion


"""
# Clase que representa el tablero del rompecabezas
"""


class Rompecabezas:
    def __init__(self, tablero):
        self.tablero = tablero
        self.ancho = len(tablero)

    @property
    def resuelto(self):
        """Verifica si el tablero está en el estado objetivo"""
        N = self.ancho * self.ancho
        return list(itertools.chain(*self.tablero)) == list(range(1, N)) + [0]

    @property
    def manhattan(self):
        """calcula la suma de distancias manhattan de todas las fichas"""
        distancia = 0
        for i in range(self.ancho):
            for j in range(self.ancho):
                valor = self.tablero[i][j]
                if valor != 0:  # No contar el espacio vacío
                    x_obj, y_obj = divmod(valor - 1, self.ancho)
                    distancia += abs(x_obj - i) + abs(y_obj - j)
        return distancia

    @property
    def movimientos_validos(self):
        """geenra todos los movimientos posibles desde el estado actual"""
        def crear_movimiento(desde, hacia):
            return lambda: self.aplicar_movimiento(desde, hacia)

        movimientos = []
        for i, j in itertools.product(range(self.ancho), range(self.ancho)):
            # direcciones posibles: derecha, izquierda, abajo, arriba
            direcciones = {
                'DERECHA': (i, j-1),
                'IZQUIERDA': (i, j+1),
                'ABAJO': (i-1, j),
                'ARRIBA': (i+1, j)
            }
            for nombre_movimiento, (fila, col) in direcciones.items():
                if (0 <= fila < self.ancho and 0 <= col < self.ancho and
                        self.tablero[fila][col] == 0):  # solo se puede mover hacia el espacio vacío
                    movimientos.append((crear_movimiento((i, j), (fila, col)), nombre_movimiento))
        return movimientos

    def aplicar_movimiento(self, desde, hacia):
        """devuelve un nuevo tablero con el movimiento aplicado (no modifica el original)"""
        nuevo_tablero = [fila[:] for fila in self.tablero]  # copia profunda
        i, j = desde
        fila, col = hacia
        # intercambia la ficha con el espacio vacio
        nuevo_tablero[i][j], nuevo_tablero[fila][col] = nuevo_tablero[fila][col], nuevo_tablero[i][j]
        return Rompecabezas(nuevo_tablero)

    def imprimir(self):
        """imprime el tablero"""
        for fila in self.tablero:
            print(fila)
        print()



"""
EJEMPLO
"""

estado_inicial = [[5, 6, 8], [0, 4, 7], [1, 3, 2]]  # 0 representa la casilla vacia

rompecabezas = Rompecabezas(estado_inicial)
solver = AlgoritmoAEstrella(rompecabezas)

# medicion tiempos
tiempo_inicio = time.perf_counter()
camino_solucion = solver.resolver()
tiempo_fin = time.perf_counter()

# mostrar resultados
pasos = 0
print("=== SOLUCION ===\n")
for nodo in camino_solucion:
    if nodo.movimiento:
        print(f"Movimiento: {nodo.movimiento}")
    else:
        print("Estado inicial:")
    nodo.estado_tablero.imprimir()
    pasos += 1

print(f"Total de pasos: {pasos}")
print(f"Tiempo transcurrido: {round(tiempo_fin - tiempo_inicio, 4)} segundos")
print("Distancia Manhattan todas las casillas:", rompecabezas.manhattan)
