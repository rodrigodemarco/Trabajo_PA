from base import Cliente, Libro, engine
from sqlalchemy.orm import sessionmaker
from funciones import prestar_libro

Session = sessionmaker(bind=engine)

session = Session()

cliente = Cliente(cuil=20429026201, nombre="Agustín", edad=23)
cliente_2 = Cliente(cuil=20429026202, nombre="María", edad=24)
cliente_3 = Cliente(cuil=20429026208, nombre="José", edad=25)
cliente_4 = Cliente(cuil=20429026209, nombre="aaaa", edad=28)

libro = Libro(titulo="Misery", autor="Stephen King", resumen="a")
libro2 = Libro(titulo="19Q4", autor="Haruki Murakami", resumen="e")
libro3 = Libro(titulo="Crimen y Castigo", autor="Fiódor Dostoyesvski",
                resumen="i")
libro4 = Libro(titulo="Indigno de ser humano", autor="Osamu Dazai",
                resumen="o")

#La operación de asociar funciona como una lista
session.add(cliente)
session.add_all([cliente_2, cliente_3, cliente_4])
session.add_all([libro, libro2, libro3, libro4])

session.commit()

prestar_libro(cliente_4, libro2)
prestar_libro(cliente_2, libro2)

session.commit()

print(cliente.libros_alq)
print(cliente_2.libros_alq)
print(libro2.alquilado_por)