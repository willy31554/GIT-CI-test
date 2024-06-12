# test_my_module.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



# Import the module you want to test
import my_module

# Define test functions using pytest
def test_addition():
    assert my_module.add(1, 2) == 3

def test_subtraction():
    assert my_module.subtract(5, 3) == 2

# Add more test functions as needed
