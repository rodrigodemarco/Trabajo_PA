#Comprueba que el libro no esté alquilado antes de asignarlo a un cliente
def prestar_libro(cliente, libro):
    if libro.alquilado_por == None:
        cliente.libros_alq.append(libro)
    else:
        print(f"El libro actualmente está alquilado por {libro.alquilado_por}")

def sumar_copias_disponibles(session, titulo):
    libros = session.query(Libro).filter(Libro.titulo == titulo).all()
    if libros:
        copias_totales = sum(libro.copias_disponibles for libro in libros)
        print(f"El libro '{titulo}' tiene {copias_totales} copias disponibles.")
        return copias_totales
    else:
        print(f"No se encontraron libros con el título '{titulo}'.")
        return 0
