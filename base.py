from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column


url_base = "sqlite:///database1.db"

engine = create_engine(url_base)

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)


class Libro(BaseModel):
    __tablename__ = "libros"

    titulo = Column(String)
    autor = Column(String)
    resumen = Column(String)
    id_cliente = Column(ForeignKey("clientes.id"))
    alquilado_por = relationship("Cliente", back_populates="libros_alq")

    def __repr__(self):
        return self.titulo
    
class Cliente(BaseModel):
    __tablename__ = "clientes"

    cuil = Column(Integer, unique=True)
    nombre = Column(String)
    edad = Column(Integer)

    libros_alq = relationship("Libro", back_populates="alquilado_por")

    def __repr__(self):
        return self.nombre

Base.metadata.drop_all(engine) #BORRA TODO EL CONTENIDO
Base.metadata.create_all(engine)