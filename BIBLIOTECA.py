class libro:

    def _init_( self, titulo, autor, genero, num_paginas):

        self.titulo = titulo

        self.autor = autor

        self.genero = genero

        self.num_paginas = num_paginas
        

        def mostrar_info(self):

               print("Titulo:", self.titulo)

               print("Autor:", self.autor)

               print("Genero:", self.genero)

               print("Numero paginas:", self.num_paginas)
        

class libro_prestado(libro):

    def _init_(self, titulo, autor, genero, num_paginas, prestado_a):

        super()._init_ (titulo, autor. genero, num_paginas)

        self.prestado_a = prestado_a


    def mostrar_info(self):
        super().mostrar_info()

        print("Prestado a:", self.prestado_a)
        

#Crear objetos en la clase libro
libro1 = libro("El codigo Da vinco", "Dan brown", "Misterio", 624,)
libro2 = libro("Cien años de soledad", "Gabriel Garcia Marquez", "Realismo magico", 432,)


#Mostrar informacion de los libros
jls_extract_var = print
jls_extract_var(" Informacion del libro 1")

libro1.mostrar_info()

print(" Informacion del libro 2")

libro2.mostrar_info()


#Crear informacion de la clase libros prestados

libro_prestado1 = libro_prestado("Python Crash Course", "Eric Matthes", "Programacion", 544, "Juan perez")

libro_prestado2 = libro_prestado("Clean Code", "Robert C. Martin", "Programacion", 464, "Maria Gomez")


#Mostrar informacion de los libros prestados

print("\Informacion del libro prestado 1:")

libro_prestado1.mostrar_info()

print("\Informacion del libro prestado 2:")

libro_prestado2.mostrar_info()