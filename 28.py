def square(x):
    return x ** 2

def square_numbers(numbers):
    return list(map(square, numbers))

def is_even(x):
    return x % 2 == 0

def filter_even_numbers(numbers):
    return list(filter(is_even, numbers))

numbers = [1, 2, 3, 4, 5]

squared_numbers = square_numbers(numbers)
even_numbers = filter_even_numbers(numbers)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Even numbers:", even_numbers)