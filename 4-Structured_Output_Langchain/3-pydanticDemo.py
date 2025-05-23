# from pydantic import BaseModel

# class Student(BaseModel):
#     name : str 

# newStudent = {'name' : "Ravendra"}

# student = Student(**newStudent)

# print(student)

# ______________________________________________________
# from pydantic import BaseModel
# from typing import Optional

# # Default Value
# class Student(BaseModel):
#     name : str = "Rv"
#     age : Optional[int] = None

# # coercing : '21'(string) will convert into 21(int)
# # newStudent = {'name' : 'Ravendra' , 'age' : 21}
# newStudent = {'name' : 'Ravendra' , 'age' : '21'}

# student = Student(**newStudent)

# print(student)


# Email __________________________________________________

from pydantic import BaseModel , EmailStr , Field
from typing import Optional

# Default Value
class Student(BaseModel):
    name : str = "Rv"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0 , lt=10 , description="A decimal value of cgpa of student")


newStudent = {'name' : 'Ravendra' , 'age' : '21' , 'email' : 'ras@gmail.com' , 'cgpa' : 5.6}

student = Student(**newStudent)

student = dict(student)

print(student['name'])