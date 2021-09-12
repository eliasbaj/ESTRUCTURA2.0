class Lista:
    def __init__(self,tamanio=4):
        self.lista = []
        self.longuitud = 0
        self.size = tamanio
    
    def insertar(self,valor):
        i=0
        enc = False
        while i < len(self.lista) and enc:
            if self.lista[i]==valor:
                enc=True
            i=i=+1
        if enc:
            self.lista= self.lista[:1]+[valor]+self.lista[i:]
            self.longuitud+=1
        return enc
    
    def append(self,dato):
        if self.longuitud < self.size:
            self.lista += [dato]
            self.longuitud += 1
            return True
        else:
            return False 
lista1 = Lista()
lista1.append(2)                
lista1.append(5)                
lista1.append(20)
print(lista1.insertar(5))         