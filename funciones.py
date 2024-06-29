from base import Libro, Cliente, Prestacion
import pandas as pd
import datetime as dt

#Comprueba que el libro no esté alquilado antes de asignarlo a un cliente
def prestar_libro(cli, lib, fecha = None):
    if lib.copias_disponibles > 0:
        lib.remover_copia()
        return Prestacion(cliente=cli, libro=lib, fecha_prest = fecha)
    else:
        print(f"El libro no cuenta con copias disponibles")

def devolver_libro(session, prest):
    libro_devuelto = session.query(Libro).filter(Libro.id == prest.id_libro).all()
    session.delete(prest)
    session.commit()
    libro_devuelto[0].agregar_copia()

#Devuelve aquellas prestaciones que ya pasaron de término
def mostrar_vencidos(session):
    prestaciones = session.query(Prestacion).all()
    for i in prestaciones:
        if i.calcular_dev() < dt.datetime.combine(dt.date.today(), dt.time.min):
            dias_vencidos = dt.datetime.combine(dt.date.today(), dt.time.min) - i.calcular_dev()
            print(f"{i.cliente} id: {i.id_cliente}, debe retornar {i.libro}. Alquiler vencido por {dias_vencidos.days} días.")

#Retorna la cantidad de copias disponibles de un libro
def sumar_copias_disponibles(session, titulo):
    libros = session.query(Libro).filter(Libro.titulo == titulo).all()
    if libros:
        copias_totales = sum(libro.copias_disponibles for libro in libros)
        print(f"El libro '{titulo}' tiene {copias_totales} copias disponibles.")
        return copias_totales
    else:
        print(f"No se encontraron libros con el título '{titulo}'.")
        return 0
