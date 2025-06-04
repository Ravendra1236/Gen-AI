# When we want to have async version or to handle concurrency
from langchain.tools import BaseTool  # Changed from BaseModel
from pydantic import BaseModel, Field  # Added pydantic imports
from typing import Type

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first Number to multiply")  # Fixed syntax
    b: int = Field(required=True, description="The second Number to multiply")  # Fixed syntax
    
class MultiplyTool(BaseTool):  # Changed from BaseModel to BaseTool
    name: str = "multiply"
    description: str = "multiply 2 numbers"
    args_schema: Type[BaseModel] = MultiplyInput
    
    def _run(self, a: int, b: int) -> int:
        return a * b
    
    def _arun(self, a: int, b: int) -> int:
        # Async implementation if needed
        raise NotImplementedError("Async version not implemented")

# Create tool instance
multiply_tool = MultiplyTool()

# Test the tool
result = multiply_tool.run({"a": 2, "b": 10})  # Changed from direct call to run()
print(result)