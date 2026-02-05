from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import employee, attendance
from app.database import engine
from app.models import Base

# Creates database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

# BROADEST CORS SETTINGS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allows all domains (Netlify, localhost, etc.)
    allow_credentials=False,  # Required to be False when using "*"
    allow_methods=["*"],      # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],      # Allows all custom headers
)

# Routes
app.include_router(employee.router, prefix="/employees", tags=["Employees"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])

@app.get("/")
def root():
    return {"message": "HRMS Lite Backend is running"}