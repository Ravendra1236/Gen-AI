# Important

from langchain_core.tools import tool 

# Step1: Create a function
# def multiply(a,b):
#     """Multiply 2 numbers"""
#     return a*b

# Step2: Add type hints
# def multiply(a:int , b:int) ->int:
#     """Multiply 2 numbers"""
#     return a*b

# Step3: Add tool decorator

@tool
def multiply(a:int , b:int) ->int:
    """Multiply 2 numbers"""
    return a*b

result = multiply.invoke({"a" : 2 , "b": 4})

print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)

# LLM does not sees tool actually this tool gets converteed into a JSON_schema
# Whenver we connect tool and schema so we send LLM json_schema of tool
# print(multiply.args_schema.model_json_schema())


# @tool 
# def addition(a:int , b:int)->int:
#     """Add 2 numbers"""
#     return a+b

# print(addition.invoke({"a" : 2 , "b" : 10} ))
