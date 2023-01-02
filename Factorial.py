def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test the function with some values
print(factorial(0))  
print(factorial(1))  
print(factorial(5))  
print(factorial(10))  
