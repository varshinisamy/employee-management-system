from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    role: str
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
