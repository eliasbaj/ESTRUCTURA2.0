class Lista ():
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud +=1
            return self.lista
        else:
            print("Lista esta llena")
            
    def obtenerEliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista = self.lista[:dato] + self.lista[dato+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux += [self.lista[indice]]
                self.longitud -= 1
                self.lista = listaAux
            return [self.lista,eliminado]
        
    def mostrar(self):
        print(" {:6} {}".format("lista","Posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:6}] {:3}".format(ele,pos))

    def buscar(self,valor):
        if valor in self.lista:
            print("Encontrado en la lista existe  el elemento", valor)
            return True
        else:
            print("No existe en la lista el elemento ", valor)
            return False
        
    def insertar(self,valor):
        if (self.buscar(valor)):
                print("No se puede insertar, ya se encuentra en la lista")
        else:
            print("El elemento  " "{}""  si se puede insertar es un nuevo elemento  para la lista ".format(valor))
            self.lista.append(valor)

    def eliminarLista(self,valor):
        def eliminarLista(self, valor):
            print("Lista original :", self.lista)
        for item in self.lista:
            if (item == valor):
                self.lista.remove(valor) 
        print("Elemento eliminado, lista queda asi:¨",self.lista)                        
    
            
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]
     #busca un dato en la lista y retorna la posicion de ese valor en la lista    
    
            
   #busca un dato con el metodobuscar y si no lo encuentro inserte           
   
         
    # busca el dato eliminar con el metodo buscar y lo elimina de lista 
   
    
            
    
   
lista1 = Lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(32)
lista1.append("Milagro")
# pos=lista1.buscar(52)
lista1.insertar(68)

# if dato:print("El elemento se encuentra en la lista:{}".format(dato))
# else : print("El elemento no se encuentra en la lista")
# lista1.mostrar()
# print(lista)

# posicion=int(input("Ingrese posicion:"))
# resp = lista1.obtenerEliminado(posicion)
# if resp == None:
#     print("Posicion no Valida")
# else:
#     print("El elemento de la posicion: {} es: {}".format(posicion,resp))
     