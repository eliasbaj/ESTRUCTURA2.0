class Matriz:
    def __init__(self,matriz):
        self.matriz=matriz
    
    def ingresar(self,dato):
        pass
    
    def presentar (self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()
    
    def buscar(self,valor):
        enc = {}
        fila= 0
        band= True
        while fila < len(self.matriz) and band:
            col=0
            while col <len(self.matriz[fila]) and band:
                if self.matriz[fila][col] == valor:
                    enc["fila"]=fila
                    enc["col"]=col
                    band= False
                else: col += 1
            fila += 1
        return enc 
                
# columnas   0  1  2    0  1  2    0  1  2
numeros = [[10,20,30],[60,80,40],[25,35,55]]
# filas         0          1          2
mat=Matriz(numeros)
resp = mat.buscar(60)
if resp: print("El valor se encuentra en las siguientes corrdenadas ", resp)
else: print("No existe el valor en la matriz")