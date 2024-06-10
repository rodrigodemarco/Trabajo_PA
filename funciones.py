
#Comprueba que el libro no esté alquilado antes de asignarlo a un cliente
def prestar_libro(cliente, libro):
    if libro.alquilado_por == None:
        cliente.libros_alq.append(libro)
    else:
        print(f"El libro actualmente está alquilado por {libro.alquilado_por}")