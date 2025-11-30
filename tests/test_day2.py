"""
Tests for Day 2: Numbers and Math Operations
"""
import math
import pytest
from src.learn_python.days_1_10 import day2_numbers


class TestDay2:
    """Test class for Day 2 numbers and math"""

    def test_math_operations(self):
        """Test basic math operations"""
        assert 2 + 3 == 5
        assert 10 - 3 == 7
        assert 4 * 5 == 20
        assert 10 / 2 == 5
        assert 10 // 3 == 3  # Floor division
        assert 10 % 3 == 1  # Modulus
        assert 2 ** 3 == 8  # Exponentiation

    def test_math_functions(self):
        """Test math functions"""
        assert abs(-5) == 5
        assert round(3.7) == 4
        assert math.sqrt(16) == 4.0
        assert math.sqrt(25) == 5.0

    def test_arithmetic_operations(self):
        """Test arithmetic operations"""
        a = 10
        b = 3

        assert a + b == 13
        assert a - b == 7
        assert a * b == 30
        assert a // b == 3
        assert a % b == 1
        assert a ** b == 1000

    def test_day2_function_runs(self):
        """Test that day2_numbers function runs without errors"""
        try:
            day2_numbers()
        except Exception as e:
            pytest.fail(f"day2_numbers() raised {e} unexpectedly")

