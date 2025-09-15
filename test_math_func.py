#import math_func
from math_func import factorial, is_prime, area_of_circle
import pytest
import math

def test_factorial_valid():
    assert factorial(4) == 24

def test_factorial_invalid_zero():
    with pytest.raises(ValueError, match="Factorial is not defined"):
        factorial(0)

def test_is_prime_valid():
    assert is_prime(7) is True
    assert is_prime(4) is False
    assert is_prime(10) is True

def test_is_prime_zero():
    assert is_prime(0) is False
    assert is_prime(1) is False
    

def test_area_of_circle_valid():
    assert area_of_circle(2) == math.pi * 4

def test_area_of_circle_zero():
    with pytest.raises(ValueError) as e:
        area_of_circle(0)
        assert "Radius must be greater than zero." in str(e.value)
