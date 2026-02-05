from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import employee, attendance
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

# redirect_slashes=False is VITAL for CORS success with Axios
app = FastAPI(title="HRMS Lite API", redirect_slashes=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # THIS IS THE HEADER: Access-Control-Allow-Origin: *
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee.router)
app.include_router(attendance.router)

@app.get("/")
def root():
    return {"message": "HRMS Lite Backend is running"}