from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app import schemas, crud, models

# Create router with explicit redirect_slashes=False to prevent automatic redirects
router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
    redirect_slashes=False          # ← Prevents redirect from /employees → /employees/
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET /employees and GET /employees/ - both supported
@router.get("", response_model=List[schemas.EmployeeResponse])
@router.get("/", response_model=List[schemas.EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    """
    Retrieve all employees
    """
    employees = crud.get_all_employees(db)
    return employees


# POST /employees and POST /employees/ - both supported
@router.post(
    "",
    response_model=schemas.EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
@router.post(
    "/",
    response_model=schemas.EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def add_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new employee
    """
    # Check if employee with same ID or email already exists
    existing = crud.get_employee_by_id_or_email(
        db, 
        employee_id=employee.employee_id, 
        email=employee.email
    )
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Employee with this ID or email already exists"
        )

    new_employee = crud.create_employee(db, employee)
    return new_employee


# DELETE /employees/{employee_id}
@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """
    Delete an employee by ID
    """
    employee = db.query(models.Employee).filter(
        models.Employee.employee_id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()
    # 204 No Content - return nothing
    return None


# Optional: Add a GET by ID endpoint (very useful for frontend)
@router.get("/{employee_id}", response_model=schemas.EmployeeResponse)
@router.get("/{employee_id}/", response_model=schemas.EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """
    Get a single employee by ID
    """
    employee = crud.get_employee(db, employee_id=employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return employee