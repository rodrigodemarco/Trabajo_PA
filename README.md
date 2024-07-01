# Trabajo Práctico de Programación Avanzada

## SQLAlchemy - Sistema Gestor de Biblioteca

### Grupo 11 - Integrantes

- De Marco, Rodrigo
- Parisi, Agustín Luciano
- Pedrol, Juan Manuel

### Cronograma

- **3/06**: Primera clase de definición de tema y metodología
- **9/06**: Selección de la librería y armado inicial de la base
- **10/06**: Clase de consulta
- **22/06 - 29-06**: Implementación en código de sugerencias y elaboración del ppt
- **30/06**: Confección del video explicativo

### Import de la librería y adicionales

```ruby
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, Mapped
import datetime as dt
```
### Declaración de la Base

declarative_base() se encarga de crear la base dado un engine, que a su vez tiene un url. En este caso corresponde al gestor de bases de datos sqlite, por lo que la base será almacenada localmente en un archivo en la computadora del usuario. La clase BaseModel será heredada por cada una de las tablas, y les otorga un id único que servirá de llave primaria.

```ruby
url_base = "sqlite:///database1.db"

engine = create_engine(url_base)

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
```

La base cuenta con tres tablas: "clientes", "libros" y "prestaciones".

## Funciones Disponibles

prestar_libro:
Esta función asigna un libro a un cliente si hay copias disponibles.
- Parámetros:
    - cli: el cliente que quiere alquilar el libro.
    - lib: el libro que se quiere alquilar.
    - fecha (opcional): la fecha en la que se presta el libro.
- Proceso:
    - Comprueba si el libro tiene copias disponibles.
    - Si hay copias disponibles, reduce la cantidad de copias disponibles y crea un objeto Prestación que representa el alquiler del libro.
    - Si no hay copias disponibles, imprime un mensaje indicando que no hay copias disponibles.

devolver_libro:
Esta función gestiona la devolución de un libro.
- Parámetros:
    - session: la sesión de la base de datos.
    - prest: el objeto Prestacion que representa el alquiler a devolver.
- Proceso:
    - Busca el libro asociado al alquiler en la base de datos.
    - Elimina el registro de Prestación.
    - Añade una copia disponible al libro devuelto.

mostrar_vencidos:
Esta función muestra los alquileres que han excedido su tiempo de préstamo.
- Parámetros:
    - session: la sesión de la base de datos.
- Proceso:
    - Obtiene todas las prestaciones de la base de datos.
    - Para cada prestación, comprueba si la fecha de devolución es anterior a la fecha actual.
    - Si el alquiler está vencido, imprime información sobre el cliente, el libro y cuántos días ha pasado el vencimiento.

sumar_copias_disponibles:
Esta función retorna la cantidad total de copias disponibles de un libro específico.
- Parámetros:
    - session: la sesión de la base de datos.
    - titulo: el título del libro.
- Proceso:
    - Busca libros con el título especificado en la base de datos.
    - Suma las copias disponibles de todos los libros encontrados.
    - Imprime y retorna la cantidad total de copias disponibles.

exportar_prestaciones:
Esta función exporta los datos de las prestaciones a un archivo CSV.
-Parámetros:
    - session: la sesión de la base de datos.
- Proceso:
    - Obtiene todas las prestaciones de la base de datos.
    - Crea un DataFrame de pandas con las prestaciones.
    - Guarda el DataFrame en un archivo CSV llamado "prestaciones.csv".

exportar_clientes:
Esta función exporta los datos de los clientes a un archivo CSV.
- Parámetros:
    - session: la sesión de la base de datos.
- Proceso:
    - Obtiene todos los clientes de la base de datos.
    - Crea un DataFrame de pandas con los clientes.
    - Guarda el DataFrame en un archivo CSV llamado "clientes.csv".

exportar_libros:
Esta función exporta los datos de los libros a un archivo CSV.
- Parámetros:
    - session: la sesión de la base de datos.
- Proceso:
    - Obtiene todos los libros de la base de datos.
    - Crea un DataFrame de pandas con los libros.
    - Guarda el DataFrame en un archivo CSV llamado "libros.csv".
