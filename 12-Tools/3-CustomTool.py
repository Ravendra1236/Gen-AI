# Using Structured Tool and Pydantic : Important
from langchain.tools import StructuredTool
from pydantic import BaseModel , Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True , description="The first number to add.")
    b:int = Field(required=True , description="The second number to add.")
    
    
def multiply_func(a,b):
    return a*b

multiplyTool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Add 2 numbers",
    args_schema=MultiplyInput
)

result = multiplyTool.invoke({"a":3 , "b":5})
print(result)
print(multiplyTool.name)
print(multiplyTool.description)
print(multiplyTool.args)