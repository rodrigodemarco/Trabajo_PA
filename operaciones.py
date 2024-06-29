from sqlalchemy.orm import sessionmaker
from base import Cliente, Libro, engine
from funciones import *
import datetime as dt

Session = sessionmaker(bind=engine)
session = Session()

# Creamos clientes y libros
cliente_1 = Cliente(cuil=1111, nombre="Agustín", edad=23)
cliente_2 = Cliente(cuil=2222, nombre="Juan", edad=24)
cliente_3 = Cliente(cuil=3333, nombre="Rodrigo", edad=25)
cliente_4 = Cliente(cuil=4444, nombre="María", edad=28)

libro_1 = Libro(titulo="Misery", autor="Stephen King", resumen="...", copias_disponibles=3)
libro_2 = Libro(titulo="1Q84", autor="Haruki Murakami", resumen="...", copias_disponibles=2)
libro_3 = Libro(titulo="Crimen y Castigo", autor="Fiódor Dostoyevski", resumen="...", copias_disponibles=1)
libro_4 = Libro(titulo="Indigno de ser humano", autor="Osamu Dazai", resumen="...", copias_disponibles=4)

# Añadimos clientes y libros a la sesión
session.add_all([cliente_1, cliente_2, cliente_3, cliente_4])
session.add_all([libro_1, libro_2, libro_3, libro_4])
session.commit()

# Vemos cómo varían las copias disponibles de los libros
sumar_copias_disponibles(session, "1Q84")
libro_2.agregar_copia()
sumar_copias_disponibles(session, "1Q84")
libro_2.remover_copia()
sumar_copias_disponibles(session, "1Q84")

# Prestado de libros
prest_1 = prestar_libro(cliente_4, libro_2)
prest_2 = prestar_libro(cliente_2, libro_2, dt.datetime(year=2024, month=3, day=10))
prest_3 = prestar_libro(cliente_2, libro_4)
session.add_all([prest_1, prest_2, prest_3])
session.commit()

#Vemos qué pasa cuando se presta un libro sin copias
sumar_copias_disponibles(session, "1Q84")
prest_4 = prestar_libro(cliente_4, libro_2)

#Vemos quiénes deben libros
mostrar_vencidos(session)

#Recuperamos el libro del alquiler vencido
devolver_libro(session, prest_2)
sumar_copias_disponibles(session, "1Q84")

#Exportamos a un csv
exportar_prestaciones(session)
exportar_clientes(session)
exportar_libros(session)

