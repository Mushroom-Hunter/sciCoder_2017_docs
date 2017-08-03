#!/usr/bin/env python

# Contributed by Justin Gilmer

# Example demonstrating how to test a list of values
# in the py.test environment without writing
# an individual "test_" function for each one.

from fizzbuzz import fizzbuzz
import pytest

# useful when using same test function on multiple outputs
@pytest.mark.parametrize("in_val, out", [
    (1,1),
    (2,2),
    (3,'fizz'),
    (4,4),
    (5,'buzz'),
    (6,'fizz'),
    (7,7),
    (8,8),
    (9,'fizz'),
    (10,'buzz'),
    (15, 'fizzbuzz'),
    ])
def test_remaining(in_val, out):
    assert(fizzbuzz(in_val) == out)

