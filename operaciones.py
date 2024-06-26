from sqlalchemy.orm import sessionmaker
from base import Cliente, Libro, engine
from funciones import prestar_libro, sumar_copias_disponibles

Session = sessionmaker(bind=engine)
session = Session()

# Creamos clientes y libros
cliente = Cliente(cuil=20429026201, nombre="Agustín", edad=23)
cliente_2 = Cliente(cuil=20429026202, nombre="María", edad=24)
cliente_3 = Cliente(cuil=20429026208, nombre="José", edad=25)
cliente_4 = Cliente(cuil=20429026209, nombre="aaaa", edad=28)

libro = Libro(titulo="Misery", autor="Stephen King", resumen="a", copias_disponibles=3)
libro2 = Libro(titulo="19Q4", autor="Haruki Murakami", resumen="e", copias_disponibles=2)
libro3 = Libro(titulo="Crimen y Castigo", autor="Fiódor Dostoyevski", resumen="i", copias_disponibles=1)
libro4 = Libro(titulo="Indigno de ser humano", autor="Osamu Dazai", resumen="o", copias_disponibles=4)

# Añadimos clientes y libros a la sesión
session.add(cliente)
session.add_all([cliente_2, cliente_3, cliente_4])
session.add_all([libro, libro2, libro3, libro4])
session.commit()

# Prestado de libros
prestar_libro(session, cliente_4, libro2)
prestar_libro(session, cliente_2, libro2)

# Sumamos copias disponibles
sumar_copias_disponibles(session, "Misery")
sumar_copias_disponibles(session, "19Q4")
