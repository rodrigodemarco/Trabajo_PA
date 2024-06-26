from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

url_base = "sqlite:///database1.db"

engine = create_engine(url_base)

Base = declarative_base()

class BaseModel(Base):
    _abstract_ = True

    id = Column(Integer, primary_key=True)

class Libro(BaseModel):
    _tablename_ = "libros"

    titulo = Column(String)
    autor = Column(String)
    resumen = Column(String)
    id_cliente = Column(ForeignKey("clientes.id"))
    copias_disponibles = Column(Integer, default=1)
    alquilado_por = relationship("Cliente", back_populates="libros_alq")

    def _repr_(self):
        return self.titulo

class Cliente(BaseModel):
    _tablename_ = "clientes"

    cuil = Column(Integer, unique=True)
    nombre = Column(String)
    edad = Column(Integer)

    libros_alq = relationship("Libro", back_populates="alquilado_por")

    def _repr_(self):
        return self.nombre

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
