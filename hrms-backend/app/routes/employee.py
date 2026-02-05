from fastapi import APIRouter as _APIRouter
from fastapi.types import DecoratedCallable
from typing import Any, Callable

class NoRedirectRouter(_APIRouter):
    def add_api_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        include_in_schema: bool = True,
        **kwargs: Any
    ) -> None:
        # Add the alternate path without slash (or with) and hide from docs
        if path.endswith("/"):
            alt_path = path[:-1]
        else:
            alt_path = path + "/"
        
        super().add_api_route(
            alt_path,
            endpoint,
            include_in_schema=False,  # Don't duplicate in Swagger
            **kwargs
        )
        
        # Add the original path normally
        super().add_api_route(
            path,
            endpoint,
            include_in_schema=include_in_schema,
            **kwargs
        )

# Use this instead of APIRouter
router = NoRedirectRouter(
    prefix="/employees",
    tags=["Employees"]
)

# Now define your endpoints ONLY ONCE — with your preferred style (e.g. no trailing slash)
@router.get("", response_model=list[schemas.EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)

# Do the same for POST (only define once)
@router.post("", response_model=schemas.EmployeeResponse, status_code=201)
def add_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    result = crud.create_employee(db, emp)
    if not result:
        raise HTTPException(status_code=409, detail="Employee ID or Email already exists")
    return result

# DELETE and any others stay as-is (they have {employee_id} so no slash issue)