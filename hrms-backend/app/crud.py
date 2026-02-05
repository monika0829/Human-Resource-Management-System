from sqlalchemy.orm import Session
from .models import Employee, Attendance
from datetime import date, time,datetime
from app import schemas, models
from fastapi import HTTPException

def create_employee(db: Session, emp):
    try:
        existing = db.query(Employee).filter(
            (Employee.employee_id == emp.employee_id) |
            (Employee.email == emp.email)
        ).first()

        if existing:
            return None

        new_emp = Employee(**emp.dict())
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp) 
        return new_emp
    except Exception as e:
        db.rollback()
        raise e

def mark_attendance(db: Session, data: schemas.AttendanceCreate):
    # Check employee exists
    employee = db.query(models.Employee).filter(
        models.Employee.employee_id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    today = date.today()

    # Prevent duplicate attendance for same day
    existing = db.query(models.Attendance).filter(
        models.Attendance.employee_id == data.employee_id,
        models.Attendance.date == today
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for today"
        )

    attendance = models.Attendance(
        employee_id=employee.id,
        date=today,
        status=data.status,
        check_in_time=datetime.now().time()
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance) 

    return attendance


def get_all_employees(db: Session):
    return db.query(Employee).all()
