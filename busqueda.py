class Lista:
    def __init__(self, listas):
        self.__lista = listas
    
    @property
    def lista(self): #getproperty
        return self.__lista  
      
    # @lista.setter
    # def lista(self, value): #getproperty
    #     return self.__lista==value  
    
    #Busca un valor en la lista; retorna la posición si lo encuentra
    # y si no lo encuentra retorna -1     
    def busquedaLineal(self, buscado):
        pos=0
        enc=False
        lon=len(self.__lista)
        #recorre la lista hasta que la posicion sea igual a la longitud y encontrado sea igual a True, o encontrado sea verdadero
        while pos < lon and enc==False:
            if self.__lista[pos]["nombre"]==buscado:
                enc=True
                break
            else:
                pos=pos+1
        if enc: return pos
        else: return -1
                    
    def ordenar(self, orden):
        orden = orden.lower()
        if orden =="asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self._lista[pos]["nombre"] > self._lista[sig]["nombre"]:
                        aux = self.__lista[pos]
                        self._lista[pos]=self._lista[sig]
                        self.__lista[sig]=aux
        else:
            if orden =="des":
                for pos in range(0,len(self.__lista)):
                    for sig in range(pos+1,len(self.__lista)):
                        if self._lista[pos]["nombre"] < self._lista[sig]["nombre"]:
                            aux = self.__lista[pos]
                            self._lista[pos]=self._lista[sig]
                            self.__lista[sig]=aux
                            
                    
    def busquedaBinaria(self,buscado):
        pass
    
    
notas=[{"nombre":"Daniel", "n1":20, "n2": 40},
       {"nombre":"Danny", "n1":30, "n2": 50},
       {"nombre":"Dayana", "n1":40, "n2": 50},
       {"nombre":"Erick", "n1":50, "n2": 40},
       {"nombre":"Romina", "n1":55, "n2": 40},
       {"nombre":"Yady", "n1":60, "n2": 40}
]

bus = Lista(notas)
# bus.lista=[3,5]
posición=bus.busquedaLineal("Erick")
if posición!=-1:
    print(bus.lista[posición])
else:
    print("Nombre, no se encuentra en la lista")

bus.ordenar("des")
print(bus.lista)