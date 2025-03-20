# Write a Python program to check if a number is prime.
n = int(input("Input a number: "))
def is_prime(n):
    if n == 0:
        print("is not prime") 
    elif  n%2 == 0:
        print("is prime")    
    else :
        print("is not prime")
is_prime(n)
