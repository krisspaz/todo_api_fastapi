
# 📝 Todo API FastAPI

API RESTful profesional para la gestión de tareas (To-Do List) usando **FastAPI**, **SQLAlchemy** y **SQLite**. Permite crear, listar, actualizar, eliminar y exportar tareas a Excel. Documentación interactiva disponible vía Swagger UI.

---

## 🚀 Características principales

- CRUD completo de tareas (crear, leer, actualizar, eliminar)
- Cada tarea tiene título, descripción y estado (pendiente/completada)
- Exportación de tareas a Excel (`.xlsx`)
- Documentación automática en `/docs` (Swagger UI)

---

## 📦 Instalación y uso rápido

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/krisspaz/todo_api_fastapi.git
   cd todo_api_fastapi
   ```
2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   # o
   pip3 install -r requirements.txt
   ```
3. **Ejecuta el servidor:**
   ```bash
   uvicorn main:app --reload
   ```
4. **Abre la documentación interactiva:**
   - [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📚 Endpoints principales

| Método | Endpoint           | Descripción                        |
|--------|--------------------|------------------------------------|
| GET    | `/tareas/`         | Listar todas las tareas            |
| POST   | `/tareas/`         | Crear una nueva tarea              |
| PUT    | `/tareas/{id}`     | Actualizar una tarea existente     |
| DELETE | `/tareas/{id}`     | Eliminar una tarea                 |
| GET    | `/exportar/`       | Exportar tareas a archivo Excel    |

---

## 🛠️ Estructura del proyecto

```
├── main.py         # Lógica principal de la API
├── models.py       # Modelos Pydantic (validación y serialización)
├── database.py     # Modelos SQLAlchemy y conexión a DB
├── requirements.txt
├── tareas.db       # Base de datos SQLite
├── tareas.xlsx     # Exportación de tareas
├── screenshots/    # Capturas de pantalla
└── ...
```

---

## 🧪 Ejemplo de uso con `curl`

```bash
# Crear una tarea
curl -X POST "http://localhost:8000/tareas/" -H "Content-Type: application/json" -d '{"titulo": "Comprar pan", "descripcion": "Ir a la panadería", "completada": false}'

# Listar tareas
curl http://localhost:8000/tareas/
```

---

## 📸 Capturas de pantalla

### Swagger UI
![Swagger UI](./screenshots/swagger_ui.png)

### Crear tarea
![POST Tarea](./screenshots/post_tarea.png)

### Listar tareas
![GET Tareas](./screenshots/get_tareas.png)

### Actualizar tarea
![PUT Tarea](./screenshots/put_tarea.png)

### Eliminar tarea
![DELETE Tarea](./screenshots/delete_tarea.png)
![DELETE Tarea 2](./screenshots/delete_tarea2.png)

### Exportación a Excel
![Excel Export](./screenshots/excel_export.png)

---

## 🧑‍💻 Autor

Desarrollado por [krisspaz](https://github.com/krisspaz)