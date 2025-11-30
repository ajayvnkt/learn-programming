"""
Tests for Day 10: Functions
"""
import pytest
from src.learn_python.days_1_10 import day10_functions


class TestDay10:
    """Test class for Day 10 functions"""

    def test_basic_function(self):
        """Test basic function definition and call"""

        def greet(name):
            return f"Hello, {name}!"

        assert greet("Alice") == "Hello, Alice!"
        assert greet("Bob") == "Hello, Bob!"

    def test_function_with_parameters(self):
        """Test function with multiple parameters"""

        def add_numbers(a, b):
            return a + b

        assert add_numbers(5, 3) == 8
        assert add_numbers(10, 20) == 30

    def test_function_with_default_parameters(self):
        """Test function with default parameters"""

        def greet_with_title(name, title="Mr./Ms."):
            return f"Hello, {title} {name}!"

        assert greet_with_title("Smith") == "Hello, Mr./Ms. Smith!"
        assert greet_with_title("Johnson", "Dr.") == "Hello, Dr. Johnson!"

    def test_variable_arguments(self):
        """Test function with *args"""

        def sum_all(*args):
            return sum(args)

        assert sum_all(1, 2, 3, 4, 5) == 15
        assert sum_all(1, 2, 3) == 6

    def test_keyword_arguments(self):
        """Test function with **kwargs"""

        def create_person(**kwargs):
            return kwargs

        person = create_person(name="Alice", age=25, city="NYC")
        assert person["name"] == "Alice"
        assert person["age"] == 25
        assert person["city"] == "NYC"

    def test_lambda_functions(self):
        """Test lambda functions"""
        square = lambda x: x ** 2

        assert square(5) == 25
        assert square(3) == 9

        # Lambda with multiple arguments
        add = lambda x, y: x + y
        assert add(2, 3) == 5

    def test_higher_order_function(self):
        """Test higher-order function"""

        def apply_operation(x, operation):
            return operation(x)

        result = apply_operation(3, lambda x: x * 2)
        assert result == 6

        result = apply_operation(5, lambda x: x ** 2)
        assert result == 25

    def test_day10_function_runs(self):
        """Test that day10_functions function runs without errors"""
        try:
            day10_functions()
        except Exception as e:
            pytest.fail(f"day10_functions() raised {e} unexpectedly")

