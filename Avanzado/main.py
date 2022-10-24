from fastapi import FastAPI
from routes.socio import socio
from docs import tags_metadata
app = FastAPI(
    title="REST API del curso de Python",
    description="Desarrollada en Python y MongoDB",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(socio)
