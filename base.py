from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, Mapped
import datetime as dt

url_base = "sqlite:///database1.db"

engine = create_engine(url_base)

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)

class Libro(BaseModel):
    __tablename__ = "libros"

    titulo = Column(String)
    autor = Column(String)
    resumen = Column(String)
    copias_disponibles = Column(Integer, default=1)

    def agregar_copia(self):
        self.copias_disponibles += 1
    
    def remover_copia(self):
        self.copias_disponibles -= 1

    def __repr__(self):
        return self.titulo

class Cliente(BaseModel):
    __tablename__ = "clientes"

    cuil = Column(Integer, unique=True)
    nombre = Column(String)
    edad = Column(Integer)

    def __repr__(self):
        return self.nombre

class Prestacion(BaseModel):
    __tablename__ = "prestaciones"

    id_cliente = Column(ForeignKey("clientes.id"))
    id_libro = Column(ForeignKey("libros.id"))
    fecha_prest = Column(DateTime, default = dt.datetime.combine(dt.date.today(), dt.time.min))

    cliente = relationship("Cliente", backref="prestaciones")
    libro = relationship("Libro", backref="prestaciones")

    def calcular_dev(self):
        return self.fecha_prest + dt.timedelta(days=30)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
