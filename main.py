from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# 1. Configuración de la Base de Datos
# Formato: postgresql://usuario:contraseña@endpoint:puerto/nombre_bd
DATABASE_URL = "postgresql://postgres:Daniel_2419@aph-database.cy78m00i65y5.us-east-1.rds.amazonaws.com:5432/postgres"

# Creamos el "motor" de conexión
engine = create_engine(DATABASE_URL)

app = FastAPI(
    title="Core API - Implementation of Anthropotechnology",
    description="Motor lógico central para la expansión del potencial humano y evolución cognitiva.",
    version="1.2.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

@app.get("/api")
@app.get("/api/")
def root():
    return RedirectResponse(url="/api/docs")

@app.get("/api/status")
def get_status():
    # Intentamos conectar a la base de datos en tiempo real
    db_status = "Desconectada"
    try:
        with engine.connect() as connection:
            # Hacemos un ping básico a PostgreSQL
            connection.execute(text("SELECT 1"))
            db_status = "Conectada y Sincronizada"
    except OperationalError:
        db_status = "Fallo de conexión a RDS"

    return {
        "sistema": "Anthropotechnology (APH)",
        "estado_servidor": "Óptimo",
        "estado_memoria": db_status,
        "fase_actual": "Integración de Memoria Persistente",
        "mensaje": "Evaluando enlaces con AWS RDS."
    }

@app.get("/api/modulos")
def get_modulos():
    return [
        {"id": 1, "nombre": "Sistemas de Vida", "estado": "Activo", "tipo": "Algorítmico"},
        {"id": 2, "nombre": "Neuroplasticidad Activa", "estado": "En calibración", "tipo": "Cognitivo"},
        {"id": 3, "nombre": "Meta-Aprendizaje", "estado": "En desarrollo", "tipo": "Sistémico"}
    ]