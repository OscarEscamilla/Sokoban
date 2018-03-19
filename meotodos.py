class sokoban: 
    mapa = [[3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,3],
            [3,4,0,1,4,4,4,3],
            [3,4,4,4,4,2,4,3],
            [3,4,4,2,4,4,4,3],
            [3,4,4,1,4,4,4,3],
            [3,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3]]
    fila = 2
    columna = 2
    def imprimirMapa(self):  
        for x in range (0,(len(self.mapa)),1):     
            m = " "
            for i in range (0,(len(self.mapa[x])),1):
                m += str(self.mapa[x][i])
            print m
    def moverDerecha(self):
        self.fila
        self.columna
        if self.mapa[self.fila][self.columna+1] == 1: 
            if self.mapa[self.fila][self.columna+2] == 4 or self.mapa[self.fila][self.columna+2] == 2:  
                self.mapa[self.fila][self.columna] = 4
                self.columna = self.columna + 1
                self.mapa[self.fila][self.columna] = 0
                self.mapa[self.fila][self.columna+1] = 1
        if self.mapa[self.fila][self.columna+1] == 4 or self.mapa[self.fila][self.columna+1] == 2: 
            self.mapa[self.fila][self.columna] = 4
            self.columna = self.columna + 1
            self.mapa[self.fila][self.columna] = 0
        if  self.mapa[self.fila][self.columna+1] == 3:
            self.mapa[self.fila][self.columna] = 0
    def moverIzquierda(self):
        self.fila
        self.columna
        if self.mapa[self.fila][self.columna-1] == 1: 
            if self.mapa[self.fila][self.columna-2] == 4 or self.mapa[self.fila][self.columna-2] == 2: 
                self.mapa[self.fila][self.columna] = 4
                self.columna = self.columna - 1
                self.mapa[self.fila][
                    self.columna] = 0
                self.mapa[self.fila][self.columna-1] = 1
        if self.mapa[self.fila][self.columna-1] == 4 or self.mapa[self.fila][self.columna-1] == 2:
            self.mapa[self.fila][self.columna] = 4
            self.columna = self.columna - 1
            self.mapa[self.fila][self.columna] = 0
        if  self.mapa[self.fila][self.columna-1] == 3:#detiene el paso si hay una pared
            self.mapa[self.fila][self.columna] = 0
    def moverArriba(self):
        self.fila
        self.columna
        if self.mapa[self.fila-1][self.columna] == 1: #evalua para empujar caja hacia abajo
            if self.mapa[self.fila-2][self.columna] == 4 or self.mapa[self.fila-2][self.columna] == 2:  #si hay camino para seguir arrastrando la caja si no no avanza y se dentiene en pared
                self.mapa[self.fila][self.columna] = 4
                self.fila = self.fila - 1
                self.mapa[self.fila][self.columna] = 0
                self.mapa[self.fila-1][self.columna] = 1
        if self.mapa[self.fila-1][self.columna] == 4 or self.mapa[self.fila-1][self.columna] == 2: #evalua si arriba hay camino y ejecuta
            self.mapa[self.fila][self.columna] = 4
            self.fila = self.fila - 1
            self.mapa[self.fila][self.columna] = 0
        if  self.mapa[self.fila-1][self.columna] == 3:#detiene el paso si hay una pared
            self.mapa[self.fila][self.columna] = 0
    def moverAbajo(self):
        self.fila
        self.columna
        if self.mapa[self.fila+1][self.columna] == 1: #evalua par arrastrar la caja hacia arriba
            if self.mapa[self.fila+2][self.columna] == 4 or self.mapa[self.fila+2][self.columna] == 2: #si hay camino para seguir arrastrando la caja si no no avanza y se dentiene en pared
                self.mapa[self.fila][self.columna] = 4
                self.fila = self.fila + 1
                self.mapa[self.fila][self.columna] = 0
                self.mapa[self.fila+1][self.columna] = 1
        if self.mapa[self.fila+1][self.columna] == 4 or self.mapa[self.fila+1][self.columna] == 2: #si hay camino avnaza
            self.mapa[self.fila][self.columna] = 4
            self.fila = self.fila + 1
            self.mapa[self.fila][self.columna] = 0
        if  self.mapa[self.fila+1][self.columna] == 3: #detiene el paso si hay una pared
            self.mapa[self.fila][self.columna] = 0

soko = sokoban()

while True:
    soko.imprimirMapa()
    movimiento = raw_input("movimiento>> ")
    print soko.fila
    print soko.columna
    if movimiento == "d":
        soko.moverDerecha()
    if movimiento == "a":
        soko.moverIzquierda()
    if movimiento == "w":
        soko.moverArriba()
    if movimiento == "s":
        soko.moverAbajo()
    if soko.mapa[3][5] == 4:
        soko.mapa[3][5] = 2
    if soko.mapa[4][3] == 4:
        soko.mapa[4][3] = 2
    if soko.mapa[4][3] == 1 and soko.mapa[3][5] == 1:
        soko.imprimirMapa()
        print "nivel resuelto"
        break
        



