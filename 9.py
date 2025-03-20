# Write a function that returns the factorial of a number using recursion.
def factorial(n):
    if n < 0 :
        return "Factorial can't be defined for negative values"
    if n ==0 or n == 1:
        return 1
    return n* factorial(n-1)

num = int(input("enter a number"))
print(factorial(num))