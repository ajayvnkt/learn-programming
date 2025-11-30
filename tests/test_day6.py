"""
Tests for Day 6: Dictionaries
"""
import pytest
from src.learn_python.days_1_10 import day6_dictionaries


class TestDay6:
    """Test class for Day 6 dictionaries"""

    def test_dictionary_creation(self):
        """Test dictionary creation and access"""
        person = {
            "name": "Alice",
            "age": 25,
            "city": "New York",
            "occupation": "Engineer"
        }

        assert person["name"] == "Alice"
        assert person["age"] == 25
        assert person.get("age", 0) == 25
        assert person.get("nonexistent", "Unknown") == "Unknown"

    def test_dictionary_methods(self):
        """Test dictionary methods"""
        person = {"name": "Alice", "age": 25, "city": "NYC"}

        keys = list(person.keys())
        values = list(person.values())
        items = list(person.items())

        assert "name" in keys
        assert "Alice" in values
        assert ("name", "Alice") in items

    def test_dictionary_operations(self):
        """Test dictionary operations"""
        person = {"name": "Alice", "age": 25}

        # Add new key
        person["email"] = "alice@example.com"
        assert person["email"] == "alice@example.com"

        # Update existing key
        person["age"] = 26
        assert person["age"] == 26

    def test_dictionary_comprehension(self):
        """Test dictionary comprehension"""
        squares_dict = {x: x**2 for x in range(1, 6)}
        expected = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

        assert squares_dict == expected

    def test_day6_function_runs(self):
        """Test that day6_dictionaries function runs without errors"""
        try:
            day6_dictionaries()
        except Exception as e:
            pytest.fail(f"day6_dictionaries() raised {e} unexpectedly")

