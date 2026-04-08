"""
Unit tests for Exercise-5.py
"""

import io
import sys
import importlib.util
from pathlib import Path

module_name = "Exercise_5"
file_path = Path(__file__).parent / "Exercise-5.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
exercise4 = importlib.util.module_from_spec(spec)
sys.modules[module_name] = exercise4
spec.loader.exec_module(exercise4)

from Exercise_5 import (
    print_triangle_o,
    prod_list_easy,
    prod_list_rec,
    prod_list_rec_full,
)

def run_tests_ex51():
    print("Running tests for Exercise 5.1...")

    def capture_output(rows):
        buf = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = buf
        try:
            print_triangle_o(rows)
        finally:
            sys.stdout = sys_stdout
        return buf.getvalue().splitlines()

    assert capture_output(0) == []
    assert capture_output(1) == ["o"]
    assert capture_output(3) == ["  o  ", " ooo ", "ooooo"]

    print("All tests for Exercise 5.1 passed!\n")


def run_tests_ex52():
    print("Running tests for Exercise 5.2...")

    assert prod_list_easy([5]) == 5
    assert prod_list_easy([1, 2, 3, 4]) == 24
    assert prod_list_easy([10, -2, 3]) == -60
    assert prod_list_easy([0, 1, 2, 3]) == 0

    print("All tests for Exercise 5.2 passed!\n")


def run_tests_ex53():
    print("Running tests for Exercise 5.3...")

    assert prod_list_rec([7]) == 7
    assert prod_list_rec([2, 3, 4]) == 24
    assert prod_list_rec([-1, 5, 2]) == -10
    assert prod_list_rec([0, 99, 100]) == 0
    assert prod_list_rec(['a', 3]) == 'aaa'

    print("All tests for Exercise 5.3 passed!\n")


def run_tests_ex54():
    print("Running tests for Exercise 5.4...")

    assert prod_list_rec_full([2, 3, 5]) == 30
    assert prod_list_rec_full([10]) == 10
    assert prod_list_rec_full([]) == 1
    assert prod_list_rec_full([0, 1, 2]) == 0

    # Non-numeric case
    buf = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buf

    try:
        result = prod_list_rec_full(['a', 3])
    finally:
        sys.stdout = sys_stdout

    assert result is None

    print("All tests for Exercise 5.4 passed!\n")