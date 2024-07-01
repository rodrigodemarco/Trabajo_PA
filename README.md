# Trabajo Práctico de Programación Avanzada

## SQLAlchemy - Sistema Gestor de Biblioteca

### Grupo 11 - Integrantes

- De Marco, Rodrigo
- Parisi, Agustín Luciano
- Pedrol, Juan Manuel

### Cronograma

- **10/06 y 17/06**: Clases de definición de tema y metodología 
- **30/06**: Confección del video explicativo.

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

### Funciones Disponibles

