from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter(prefix="/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.delete("/{employee_id}", status_code=204)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(
        models.Employee.employee_id == employee_id
    ).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()


    return {"message": "Employee deleted successfully"}
@router.post("/",response_model=schemas.EmployeeResponse, status_code=201)
def add_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    result = crud.create_employee(db, emp)
    if not result:
        raise HTTPException(
            status_code=409,
            detail="Employee ID or Email already exists"
        )
    return result

@router.get("/")
def list_employees(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)
