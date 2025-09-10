# ✅ API de Tareas con FastAPI

API RESTful para gestionar una lista de tareas (To-Do List).  
Permite **crear, listar, actualizar, eliminar y exportar tareas a Excel**.

---

## 🚀 Funcionalidades
- CRUD de tareas (crear, leer, actualizar, eliminar).
- Cada tarea tiene título, descripción y estado (pendiente/completada).
- Exportación de tareas a Excel.
- Documentación automática en `/docs`.

---

## ▶️ Cómo correrlo
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/krisspaz/todo_api_fastapi.git
   cd todo_api_fastapi
INSTALAR DEPENDENCIAS
pip install -r requirements.txt 
pip3 install -r requirements.txt
EJECUTAR EL SERVIDOR
uvicorn main:app --reload

## 📸 Capturas ### Swagger UI ![Swagger UI](./screenshots/swagger_ui.png) 
### Crear tarea ![POST Tarea](./screenshots/post_tarea.png)
### Listar tareas ![GET Tareas](./screenshots/get_tareas.png) 
### Actualizar tarea ![PUT Tarea](./screenshots/put_tarea.png) 
### Eliminar tarea ![DELETE Tarea](./screenshots/delete_tarea.png) ![DELETE Tarea](./screenshots/delete_tarea2.png) 
### Exportación a Excel ![Excel Export](./screenshots/excel_export.png)