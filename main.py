from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd

from database import SessionLocal, Tarea
from models import TareaCreate, TareaResponse

app = FastAPI(title="API de Tareas")

# Dependencia para sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tareas/", response_model=TareaResponse)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    db_tarea = Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@app.get("/tareas/", response_model=list[TareaResponse])
def listar_tareas(db: Session = Depends(get_db)):
    return db.query(Tarea).all()

@app.put("/tareas/{tarea_id}", response_model=TareaResponse)
def actualizar_tarea(tarea_id: int, tarea: TareaCreate, db: Session = Depends(get_db)):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    for key, value in tarea.dict().items():
        setattr(db_tarea, key, value)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(db_tarea)
    db.commit()
    return {"message": "Tarea eliminada"}

@app.get("/exportar/")
def exportar_excel(db: Session = Depends(get_db)):
    tareas = db.query(Tarea).all()
    if not tareas:
        return {"message": "No hay tareas para exportar"}
    data = [{"id": t.id, "titulo": t.titulo, "descripcion": t.descripcion, "completada": t.completada} for t in tareas]
    df = pd.DataFrame(data)
    archivo = "tareas.xlsx"
    df.to_excel(archivo, index=False)
    return {"message": f"Tareas exportadas a {archivo}"}
