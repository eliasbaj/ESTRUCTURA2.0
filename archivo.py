class Texto:
    
    def leer():
         with open("estudiantes.txt", 'r', encoding="UTF-8") as f:
             for linea in f:
                 print(linea)
    
    def escribir(self):
        nombres = ['Fernada', 'Lola','Esperanza','Esther','Lucas' ]
        with open("estudiantes.txt", "w", encoding="UTF-8") as file:
            for nombre in nombres:
                file.write(nombre)
                file.write('\n')

arch1=Texto()
arch1.leer()           