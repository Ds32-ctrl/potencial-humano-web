from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Inicializamos la aplicación
app = FastAPI(
    title="Core API - Implementation of Anthropotechnology",
    description="Motor lógico central para la expansión del potencial humano y evolución cognitiva.",
    version="1.1.0"
)

# Redirección automática a la documentación de FastAPI
@app.get("/api")
def root():
    return RedirectResponse(url="/docs")

# Endpoint original mejorado
@app.get("/api/status")
def get_status():
    return {
        "sistema": "Anthropotechnology (APH)",
        "estado": "Óptimo",
        "módulos_activos": 3,
        "fase_actual": "Estructuración de Nodos Centrales",
        "mensaje": "Sincronización de datos al 100%."
    }

# Nuevo Endpoint: Catálogo de módulos
@app.get("/api/modulos")
def get_modulos():
    return [
        {"id": 1, "nombre": "Sistemas de Vida", "estado": "Activo", "tipo": "Algorítmico"},
        {"id": 2, "nombre": "Neuroplasticidad Activa", "estado": "En calibración", "tipo": "Cognitivo"},
        {"id": 3, "nombre": "Meta-Aprendizaje", "estado": "En desarrollo", "tipo": "Sistémico"}
    ]