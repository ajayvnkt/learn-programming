"""
Tests for Day 4: Lists and List Methods
"""
import pytest
from src.learn_python.days_1_10 import day4_lists


class TestDay4:
    """Test class for Day 4 lists"""

    def test_list_operations(self):
        """Test list operations"""
        numbers = [1, 2, 3]

        # Append
        numbers.append(4)
        assert numbers == [1, 2, 3, 4]

        # Insert
        numbers.insert(0, 0)
        assert numbers == [0, 1, 2, 3, 4]

        # Remove
        numbers.remove(3)
        assert numbers == [0, 1, 2, 4]

        # Pop
        popped = numbers.pop()
        assert popped == 4
        assert numbers == [0, 1, 2]

    def test_list_slicing(self):
        """Test list slicing"""
        numbers = [0, 1, 2, 3, 4, 5]

        assert numbers[:3] == [0, 1, 2]
        assert numbers[-2:] == [4, 5]
        assert numbers[::2] == [0, 2, 4]

    def test_list_comprehension(self):
        """Test list comprehension"""
        squares = [x**2 for x in range(1, 6)]
        assert squares == [1, 4, 9, 16, 25]

        # Even numbers
        evens = [x for x in range(10) if x % 2 == 0]
        assert evens == [0, 2, 4, 6, 8]

    def test_list_indexing(self):
        """Test list indexing"""
        numbers = [1, 2, 3, 4, 5]

        assert numbers[0] == 1
        assert numbers[-1] == 5
        assert numbers[2] == 3

    def test_day4_function_runs(self):
        """Test that day4_lists function runs without errors"""
        try:
            day4_lists()
        except Exception as e:
            pytest.fail(f"day4_lists() raised {e} unexpectedly")

