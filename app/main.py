from fastapi import FastAPI
from . import models, database, routes

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include API routes
app.include_router(routes.router)
