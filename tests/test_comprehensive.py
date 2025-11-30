"""
Tests for Comprehensive Problems
"""
import pytest
from src.learn_python.days_1_10 import (
    comprehensive_problem_student_grade_manager,
    comprehensive_problem_library_books,
)


class TestComprehensiveProblems:
    """Test comprehensive problems"""

    def test_student_grade_manager_runs(self):
        """Test that student grade manager runs without errors"""
        try:
            comprehensive_problem_student_grade_manager()
        except Exception as e:
            pytest.fail(f"comprehensive_problem_student_grade_manager() raised {e} unexpectedly")

    def test_library_books_runs(self):
        """Test that library books problem runs without errors"""
        try:
            comprehensive_problem_library_books()
        except Exception as e:
            pytest.fail(f"comprehensive_problem_library_books() raised {e} unexpectedly")

