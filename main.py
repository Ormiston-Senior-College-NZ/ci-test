def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calling the factorial function with a negative number
result = factorial(-5)
print(result)
