from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import employee, attendance
from app.database import engine
from app.models import Base

# This creates your database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

# Define which "origins" are allowed to talk to this API
origins = [
    "https://hrmsprojectn.netlify.app",  # Your production frontend
    "http://localhost:5173",             # Your local development
    "http://127.0.0.1:5173",             # Local development (alternative IP)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers
)

app.include_router(employee.router)
app.include_router(attendance.router)

@app.get("/")
def root():
    return {"message": "HRMS Lite Backend is running"}