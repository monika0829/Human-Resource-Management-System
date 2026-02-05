from sqlalchemy import Column, Integer, String, Date, Time, UniqueConstraint
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    check_in_time = Column(Time)

    __table_args__ = (
        UniqueConstraint("employee_id", "date"),
    )
