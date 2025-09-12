
"""
main.py
---------
API RESTful profesional para gestión de tareas usando FastAPI, SQLAlchemy y SQLite.
Incluye endpoints CRUD y exportación a Excel.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd

from database import SessionLocal, Tarea
from models import TareaCreate, TareaResponse

app = FastAPI(
    title="Todo API FastAPI",
    description="API profesional para gestión de tareas con exportación a Excel.",
    version="1.0.0",
)

def get_db():
    """Genera una sesión de base de datos para cada request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tareas/", response_model=TareaResponse, summary="Crear tarea", tags=["Tareas"])
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    """Crea una nueva tarea en la base de datos."""
    db_tarea = Tarea(**tarea.model_dump())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@app.get("/tareas/", response_model=list[TareaResponse], summary="Listar tareas", tags=["Tareas"])
def listar_tareas(db: Session = Depends(get_db)):
    """Devuelve la lista de todas las tareas."""
    return db.query(Tarea).all()

@app.put("/tareas/{tarea_id}", response_model=TareaResponse, summary="Actualizar tarea", tags=["Tareas"])
def actualizar_tarea(tarea_id: int, tarea: TareaCreate, db: Session = Depends(get_db)):
    """Actualiza una tarea existente por ID."""
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    for key, value in tarea.model_dump().items():
        setattr(db_tarea, key, value)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@app.delete("/tareas/{tarea_id}", summary="Eliminar tarea", tags=["Tareas"])
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    """Elimina una tarea por ID."""
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(db_tarea)
    db.commit()
    return {"message": "Tarea eliminada"}

@app.get("/exportar/", summary="Exportar tareas a Excel", tags=["Exportación"])
def exportar_excel(db: Session = Depends(get_db)):
    """Exporta todas las tareas a un archivo Excel (.xlsx)."""
    tareas = db.query(Tarea).all()
    if not tareas:
        return {"message": "No hay tareas para exportar"}
    data = []
    for t in tareas:
        data.append({
            "id": getattr(t, "id", None),
            "titulo": getattr(t, "titulo", ""),
            "descripcion": getattr(t, "descripcion", ""),
            "completada": getattr(t, "completada", False)
        })
    df = pd.DataFrame(data)
    archivo = "tareas.xlsx"
    df.to_excel(archivo, index=False)
    return {"message": f"Tareas exportadas a {archivo}"}
