def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

num1 = 10
num2 = 0
result = safe_divide(num1, num2)
print(result)  
