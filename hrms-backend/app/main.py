from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import employee, attendance
from app.database import engine
from app.models import Base

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

# GLOBAL CORS CONFIGURATION
# This adds the 'Access-Control-Allow-Origin' header to every response
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allows all domains (resolves the CORS policy error)
    allow_credentials=False,  # Must be False when using the "*" wildcard
    allow_methods=["*"],      # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],      # Allows all headers (Content-Type, Authorization, etc.)
)

# Important: Do not use trailing slashes in your route inclusions
app.include_router(employee.router)
app.include_router(attendance.router)

@app.get("/")
def root():
    return {"message": "HRMS Lite Backend is running"}