from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.http_resource_routers import root_resource


microservice_title = 'moon_shuttle'

# -----------------------------------------------------------------------------
# Instance of FastAPI Application
# -----------------------------------------------------------------------------
app = FastAPI(
    title="Microservice Template",
    description="A FastAPI-based template for Python-based microservices",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/",
    redoc_url=None
)


# -----------------------------------------------------------------------------
# CORS RULES
# -----------------------------------------------------------------------------
origins = [
    "*"
]

# Default configuration is to ALLOW ALL from EVERYWHERE. You might want to
# restrict this.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# ADD ROUTERS
# -----------------------------------------------------------------------------
app.include_router(root_resource.router)

