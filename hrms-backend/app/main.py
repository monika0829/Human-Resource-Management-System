from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import employee, attendance
from app.database import engine
from app.models import Base

# This creates your database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

# Setting allow_origins to ["*"] removes all origin restrictions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,  # Must be False when using wildcard "*"
    allow_methods=["*"],      # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],      # Allows all headers
)

app.include_router(employee.router)
app.include_router(attendance.router)

@app.get("/")
def root():
    return {"message": "HRMS Lite Backend is running"}