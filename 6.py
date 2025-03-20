# Generate the Fibonacci sequence up to n terms.
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive (n-1)
        seq.append(seq[-1]+ seq[-2])
        return seq
n = int(input("Enter the number of terms: "))

print(f"Fibonacci sequence up to {n} terms: {fibonacci_recursive(n)}")