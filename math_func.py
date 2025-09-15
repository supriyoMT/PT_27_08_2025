import math
import pytest

# ---------------------------
# Functions under test
# ---------------------------

def factorial(n):
    if n < 1:
        raise ValueError("Factorial is not defined for zero or negative numbers.")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def area_of_circle(r):
    if r <= 0:
        raise ValueError("Radius must be greater than zero.")
    return math.pi * r * r