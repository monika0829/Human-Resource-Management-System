from pydantic import BaseModel, EmailStr
from datetime import date

class EmployeeCreate(BaseModel):
    employee_id: int
    full_name: str
    email: EmailStr
    department: str
    
class EmployeeResponse(BaseModel):
    id: int
    employee_id: int
    full_name: str
    email: str
    department: str

    class Config:
        orm_mode = True
class AttendanceCreate(BaseModel):
    employee_id: int
    status: str  # Present / Absent


class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    date: date
    status: str
    check_in_time: str | None

    class Config:
        from_attributes = True
class AttendanceListResponse(BaseModel):
    id: int
    employee_name: str
    date: date
    status: str

    class Config:
        from_attributes = True
        
class AttendanceMark(BaseModel):
    employee_id: int
    status: str
