"""
Tests for Day 1: Python Basics - Variables, Data Types, and Print Statements
"""
import pytest
from src.learn_python.days_1_10 import day1_basics


class TestDay1:
    """Test class for Day 1 basics"""

    def test_variables(self):
        """Test variable assignments and types"""
        name = "Test"
        age = 30
        height = 6.0
        is_student = True

        assert isinstance(name, str)
        assert isinstance(age, int)
        assert isinstance(height, float)
        assert isinstance(is_student, bool)
        assert name == "Test"
        assert age == 30

    def test_data_types(self):
        """Test different data types"""
        # String
        text = "Hello"
        assert type(text) == str

        # Integer
        number = 42
        assert type(number) == int

        # Float
        decimal = 3.14
        assert type(decimal) == float

        # Boolean
        flag = True
        assert type(flag) == bool

    def test_day1_function_runs(self):
        """Test that day1_basics function runs without errors"""
        try:
            day1_basics()
        except Exception as e:
            pytest.fail(f"day1_basics() raised {e} unexpectedly")

