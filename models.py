"""
models.py
---------
Modelos Pydantic para validación y serialización de datos de tareas.
"""

from pydantic import BaseModel

class TareaBase(BaseModel):
    """Modelo base de tarea (campos comunes)."""
    titulo: str
    descripcion: str
    completada: bool = False

class TareaCreate(TareaBase):
    """Modelo para creación de tarea (input)."""
    pass

class TareaResponse(TareaBase):
    """Modelo de respuesta de tarea (output)."""
    id: int

    class Config:
        orm_mode = True  # Permite compatibilidad con ORM
