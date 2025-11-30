"""
Tests for Day 8: For Loops
"""
import pytest
from src.learn_python.days_1_10 import day8_for_loops


class TestDay8:
    """Test class for Day 8 for loops"""

    def test_basic_for_loop(self):
        """Test basic for loop"""
        fruits = ["apple", "banana", "orange"]
        result = []

        for fruit in fruits:
            result.append(fruit)

        assert result == ["apple", "banana", "orange"]

    def test_for_loop_with_range(self):
        """Test for loop with range"""
        numbers = []

        for i in range(1, 6):
            numbers.append(i)

        assert numbers == [1, 2, 3, 4, 5]

    def test_enumerate(self):
        """Test enumerate in for loop"""
        fruits = ["apple", "banana"]
        result = []

        for index, fruit in enumerate(fruits):
            result.append((index, fruit))

        assert result == [(0, "apple"), (1, "banana")]

    def test_dictionary_iteration(self):
        """Test iterating through dictionary"""
        person = {"name": "Alice", "age": 25, "city": "NYC"}
        items = []

        for key, value in person.items():
            items.append((key, value))

        assert ("name", "Alice") in items
        assert ("age", 25) in items

    def test_nested_loops(self):
        """Test nested loops"""
        result = []

        for i in range(1, 3):
            for j in range(1, 3):
                result.append((i, j, i * j))

        assert (1, 1, 1) in result
        assert (2, 2, 4) in result

    def test_day8_function_runs(self):
        """Test that day8_for_loops function runs without errors"""
        try:
            day8_for_loops()
        except Exception as e:
            pytest.fail(f"day8_for_loops() raised {e} unexpectedly")

