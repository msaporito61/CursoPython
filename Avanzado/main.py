from fastapi import FastAPI
from routes.socio import socio
from routes.cuota import cuota
from docs import tags_metadata

app = FastAPI(
    title="Rest Api del curso de Python de IBM",
    description="Desarrollada en Python y MondoDB",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(socio)
app.include_router(cuota)