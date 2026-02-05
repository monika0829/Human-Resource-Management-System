from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud
from app.models import Attendance, Employee

router = APIRouter(prefix="/attendance", tags=["Attendance"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: Mark Attendance
@router.post(
    "/mark",
    response_model=schemas.AttendanceResponse,
    status_code=201
)
def mark_attendance(
    data: schemas.AttendanceCreate,
    db: Session = Depends(get_db)
):
    result = crud.mark_attendance(db, data)

    if result == "EMPLOYEE_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Employee not found")

    return result

# GET: List Attendance Records
@router.get("/", response_model=list[schemas.AttendanceListResponse])
def list_attendance(db: Session = Depends(get_db)):
    records = (
        db.query(
            Attendance.id,
            Employee.full_name.label("employee_name"),
            Attendance.date,
            Attendance.status
        )
        .join(Employee, Attendance.employee_id == Employee.id)
        .all()
    )

    return records
