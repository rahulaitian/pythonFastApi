
def square(x):
    return x ** 2

def square_numbers(numbers):
    return list(map(square, numbers))

numbers = [1, 2, 3, 4, 5]

squared_numbers = square_numbers(numbers)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)