"""
Tests for Day 9: While Loops
"""
import pytest
from src.learn_python.days_1_10 import day9_while_loops


class TestDay9:
    """Test class for Day 9 while loops"""

    def test_basic_while_loop(self):
        """Test basic while loop"""
        count = 0
        result = []

        while count < 5:
            result.append(count)
            count += 1

        assert result == [0, 1, 2, 3, 4]

    def test_while_loop_with_condition(self):
        """Test while loop with condition"""
        number = 10
        result = []

        while number > 1:
            result.append(number)
            number = number // 2

        assert result == [10, 5, 2]

    def test_while_loop_with_break(self):
        """Test while loop with break"""
        numbers = [1, 3, 5, 6, 7, 9]
        index = 0
        found = None

        while index < len(numbers):
            if numbers[index] % 2 == 0:
                found = numbers[index]
                break
            index += 1

        assert found == 6

    def test_while_loop_with_continue(self):
        """Test while loop with continue"""
        num = 1
        odds = []

        while num <= 10:
            if num % 2 == 0:
                num += 1
                continue
            odds.append(num)
            num += 1

        assert odds == [1, 3, 5, 7, 9]

    def test_day9_function_runs(self):
        """Test that day9_while_loops function runs without errors"""
        try:
            day9_while_loops()
        except Exception as e:
            pytest.fail(f"day9_while_loops() raised {e} unexpectedly")

