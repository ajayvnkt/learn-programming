"""
Tests for Day 7: If Statements and Conditionals
"""
import pytest
from src.learn_python.days_1_10 import day7_conditionals


class TestDay7:
    """Test class for Day 7 conditionals"""

    def test_if_else(self):
        """Test basic if-else statements"""
        age = 20

        if age >= 18:
            result = "adult"
        else:
            result = "minor"

        assert result == "adult"

    def test_elif_chain(self):
        """Test elif chain"""
        score = 85

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "F"

        assert grade == "B"

    def test_logical_operators(self):
        """Test logical operators"""
        is_student = True
        has_id = True

        if is_student and has_id:
            access = "granted"
        elif is_student or has_id:
            access = "partial"
        else:
            access = "denied"

        assert access == "granted"

    def test_ternary_operator(self):
        """Test ternary operator"""
        age = 20
        status = "Eligible" if age >= 18 else "Not eligible"

        assert status == "Eligible"

        age = 15
        status = "Eligible" if age >= 18 else "Not eligible"
        assert status == "Not eligible"

    def test_day7_function_runs(self):
        """Test that day7_conditionals function runs without errors"""
        try:
            day7_conditionals()
        except Exception as e:
            pytest.fail(f"day7_conditionals() raised {e} unexpectedly")

