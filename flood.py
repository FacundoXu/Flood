from random import *

class Flood:
    '''
    Clase para administrar un tablero de N colores.
    '''
    def __init__(self, alto, ancho):
        '''
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        '''
        # Parte 1: Cambiar el `raise` por tu código...
        self.filas = alto
        self.columnas = ancho
        self.tablero = [[0 for j in range(ancho)] for i in range(alto)]
 
    def mezclar_tablero(self, n_colores):
        '''
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        '''
        # Parte 1: Cambiar el `raise` por tu código...
        def _mezclar_tablero(tablero, n_colores, i, j):
            tablero[i][j] = randint(0, n_colores - 1)

            if i == self.columnas - 1 and j == self.filas - 1:
                return

            if j + 1 < self.columnas:
                return _mezclar_tablero(tablero, n_colores, i, j + 1)

            if i + 1 < self.filas:
                return _mezclar_tablero(tablero, n_colores, i + 1, 0)

        return _mezclar_tablero(self.tablero, n_colores, 0, 0)

    def obtener_color(self, fil, col):
        '''
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        '''
        # Parte 1: Cambiar el `raise` por tu código...
        return self.tablero[fil][col]

    def obtener_posibles_colores(self):
        '''
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        '''
        # Parte 1: Cambiar el `raise` por tu código...
        def _obtener_posibles_colores(colores, i, j):

            if self.tablero[i][j] not in colores:
                colores.append(self.tablero[i][j])

            if i == self.filas - 1 and j == self.columnas - 1:
                colores.sort()
                return colores

            if j + 1 < self.columnas:
                return _obtener_posibles_colores(colores, i, j + 1)

            if i + 1 < self.filas:
                return _obtener_posibles_colores(colores, i + 1, 0)
                
        return _obtener_posibles_colores([], 0, 0)

    def dimensiones(self):
        '''
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        '''
        # Parte 1: Cambiar el `raise` por tu código...
        return (self.filas, self.columnas)

    def _cambiar_color(self, color_actual, color_nuevo, i = 0, j = 0):
        if i < 0 or i >= self.filas or j < 0 or j >= self.columnas or self.tablero[i][j] != color_actual:
            return

        self.tablero[i][j] = color_nuevo
        self._cambiar_color(color_actual, color_nuevo, i, j + 1)
        self._cambiar_color(color_actual, color_nuevo, i, j - 1)
        self._cambiar_color(color_actual, color_nuevo, i + 1, j)
        self._cambiar_color(color_actual, color_nuevo, i - 1, j)

    def cambiar_color(self, color_nuevo):
        '''
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        '''
        # Parte 2: Tu código acá...
        color_actual = self.tablero[0][0]

        if self.esta_completado() or color_actual == color_nuevo:
            return

        self._cambiar_color(color_actual, color_nuevo)

    def clonar(self):
        '''
        Devuelve:
            Flood: Copia del Flood actual
        '''
        # Parte 3: Tu código acá...
        copia_flood = Flood(self.filas, self.columnas)
        copia_flood.tablero = []
      
        for i in range(len(self.tablero)):
            copia_flood.tablero.append([])
            for j in range(len(self.tablero[0])):
                copia_flood.tablero[i].append(self.tablero[i][j])

        return copia_flood

    def esta_completado(self):
        '''
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        '''
        # Parte 4: Tu código acá...
        color_actual = self.tablero[0][0]

        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.tablero[i][j] != color_actual:
                    return False
                    
        return True

    def _comprobacion(self, copia_flood, color, i = 0, j = 0):
        '''
        Verifica recursivamente los casilleros. Si el casillero es igual al color
        actual, se le asigna '' indicando que es parte del flood actual
        '''
        cantidad = 0

        if i < 0 or i >= copia_flood.filas or j < 0 or j >= copia_flood.columnas:
            return 0
            
        if copia_flood.tablero[i][j] != color:
            return 0

        copia_flood.tablero[i][j] = ''
        cantidad += 1
        cantidad += copia_flood._comprobacion(copia_flood, color, i, j + 1)
        cantidad += copia_flood._comprobacion(copia_flood, color, i, j - 1)
        cantidad += copia_flood._comprobacion(copia_flood, color, i + 1, j)
        cantidad += copia_flood._comprobacion(copia_flood, color, i - 1, j)

        return cantidad

    def comprobacion(self):
        '''
        Devuelve:
            int: Cantidad de casilleros que ocupa el flood actual
        '''
        copia_flood = self.clonar()
        color = copia_flood.tablero[0][0]
        return self._comprobacion(copia_flood, color)