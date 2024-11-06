import math
def sin(a):
   checkNumericInput(a)
   return math.sin(math.radians(a))
    
def cos(a):
    checkNumericInput(a)
    return math.cos(math.radians(a))
def tan(a):
    checkNumericInput(a)
    return math.tan(math.radians(a))
   
def sqrt(a):
    checkNumericInput(a)
    if a < 0:
        raise ValueError("there is no squreroot of a negative number")
    return math.sqrt(a)


def log(a,b= math.e):
    checkNumericInput(a,b)
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Log a must be positive and the base cannot be negative or 1") 
    return math.log(a,b)

def exp(a):
   checkNumericInput(a)
   return math.exp(a)
    
#Helper function thats checks for numeric inputs    
def checkNumericInput(firstInput,secondInput = None):
    if not isinstance(firstInput,(int,float)):
        raise ValueError("this input must be a number")
    if secondInput is not None and not isinstance(secondInput,(int,float)):
        raise ValueError("Both inputs must be numbers")