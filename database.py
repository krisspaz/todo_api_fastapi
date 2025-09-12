"""
database.py
-----------
Configuración de la base de datos y modelo ORM para tareas.
"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./tareas.db"

# Crear motor de base de datos SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sesión de base de datos local
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base declarativa para modelos ORM
Base = declarative_base()

class Tarea(Base):
    """Modelo ORM de la tabla de tareas."""
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    completada = Column(Boolean, default=False)

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)
