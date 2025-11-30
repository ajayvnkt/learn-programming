"""
Tests for Day 5: Tuples and Sets
"""
import pytest
from src.learn_python.days_1_10 import day5_tuples_sets


class TestDay5:
    """Test class for Day 5 tuples and sets"""

    def test_tuples(self):
        """Test tuples"""
        coord = (3, 4)
        assert coord[0] == 3
        assert coord[1] == 4

        # Tuple unpacking
        x, y = coord
        assert x == 3
        assert y == 4

        # Immutability check
        person = ("Alice", 25, "Engineer")
        assert person[0] == "Alice"
        assert person[1] == 25

    def test_sets(self):
        """Test sets"""
        # Sets remove duplicates
        numbers = {1, 2, 3, 4, 5, 5, 4}
        assert len(numbers) == 5
        assert numbers == {1, 2, 3, 4, 5}

    def test_set_operations(self):
        """Test set operations"""
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}

        # Union
        assert set1 | set2 == {1, 2, 3, 4, 5, 6}
        assert set1.union(set2) == {1, 2, 3, 4, 5, 6}

        # Intersection
        assert set1 & set2 == {3, 4}
        assert set1.intersection(set2) == {3, 4}

        # Difference
        assert set1 - set2 == {1, 2}
        assert set1.difference(set2) == {1, 2}

        # Symmetric difference
        assert set1 ^ set2 == {1, 2, 5, 6}

    def test_day5_function_runs(self):
        """Test that day5_tuples_sets function runs without errors"""
        try:
            day5_tuples_sets()
        except Exception as e:
            pytest.fail(f"day5_tuples_sets() raised {e} unexpectedly")

