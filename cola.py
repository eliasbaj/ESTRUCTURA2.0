class Cola:
    def __init__(self,tamanio=1):
        self.lista = []
        self.size=tamanio
        self.tope=0

    def push(self,dato):
        if self.tope < self.size:
            self.lista = [dato] + self.lista 
            self.tope += 1
            return self.lista
        else:
            print("La lista esta llena")
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista [-1]
            self.lista = self.lista [:-1]
            self.tope -= 1  
            return top
        
    def show(self):
        for top in range (self.tope):
            print("[{}]".format(self.lista[top]))
    
    def longitud(self):
        return self.tope
                    
             
    def empty(self):
        if self.tope== 0:
            return True
        else:
            return False
    
# cola1=Cola (3)
# print(cola1.push(8))
# print(cola1.push(10))
# print(cola1.push(12))
# print(cola1.push(4))
# # dato = cola1.pop()
# if dato: print("el dato elimanado es :{}".format(dato))
# else: print(" La lista esta vacia")
# dato = cola1.pop()
# if dato: print("el dato elimanado es :{}".format(dato))
# else: print(" La lista esta vacia")
# dato = cola1.pop()
# if dato: print("el dato elimanado es :{}".format(dato))
# else: print(" La lista esta vacia")
# dato = cola1.pop()
# if dato: print("el dato elimanado es :{}".format(dato))
# else: print(" La lista esta vacia")
# cola1.show()
# print(cola1.longitud())
# dato=cola1.empty()
# if dato: print("la pila esta vacia ")
# else: print(" La pila tiene elementos")



