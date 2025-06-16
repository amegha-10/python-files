
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

a = int(input("Enter first number: "))  
b = int(input("Enter second number: ")) 

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Modulus:", modulus(a, b))

# Output:

# Enter first number: 10
# Enter second number: 3
# Addition: 13
# Subtraction: 7
# Multiplication: 30
# Division: 3.3333333333333335
# Modulus: 1
