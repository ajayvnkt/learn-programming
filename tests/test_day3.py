"""
Tests for Day 3: Strings and String Methods
"""
import pytest
from src.learn_python.days_1_10 import day3_strings


class TestDay3:
    """Test class for Day 3 strings"""

    def test_string_methods(self):
        """Test string methods"""
        text = "Hello World"

        assert text.upper() == "HELLO WORLD"
        assert text.lower() == "hello world"
        assert text.title() == "Hello World"
        assert len(text) == 11
        assert text.replace("World", "Python") == "Hello Python"

    def test_string_slicing(self):
        """Test string slicing"""
        greeting = "Hello, World!"

        assert greeting[:5] == "Hello"
        assert greeting[-6:] == "World!"
        assert greeting[2:5] == "llo"
        assert greeting[0:5] == "Hello"

    def test_string_formatting(self):
        """Test string formatting"""
        name = "Python"

        # f-string
        assert f"Hello, {name}!" == "Hello, Python!"

        # format()
        assert "Hello, {}!".format(name) == "Hello, Python!"

        # Old style
        assert "Hello, %s!" % name == "Hello, Python!"

    def test_string_split(self):
        """Test string splitting"""
        greeting = "Hello, World!"
        result = greeting.split(", ")

        assert result == ["Hello", "World!"]
        assert isinstance(result, list)

    def test_day3_function_runs(self):
        """Test that day3_strings function runs without errors"""
        try:
            day3_strings()
        except Exception as e:
            pytest.fail(f"day3_strings() raised {e} unexpectedly")

