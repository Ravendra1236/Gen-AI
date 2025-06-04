from langchain_core.tools import tool 

# Custom tool 1: Multiply
@tool
def multiply(a:int , b:int)->int:
    """Multiply 2 Numbers"""
    return a*b 


# Custom tool 2: Addition
@tool
def addition(a:int , b:int)->int:
    """Add 2 Numbers"""
    return a+b 

class MathToolKit:
    def __init__(self):
        self._addition = addition
        self._multiply = multiply

    def addition(self, a, b):
        return self._addition.invoke({"a": a, "b": b})

    def multiply(self, a, b):
        return self._multiply.invoke({"a": a, "b": b})

    def get_tools(self):
        return [self._addition, self._multiply]

toolkit = MathToolKit()

# tools = toolkit.get_tools()
# print(tools)

# result = toolkit.addition(2,3)
# print(result)

result = toolkit.multiply(2,3)
print(result)

