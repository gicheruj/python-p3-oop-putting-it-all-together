#!/usr/bin/env python3

import io
import sys

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Initialize _size to None
        self.size = size  # Use the setter to set size
        self.condition = 'New'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'


# Test cases

def test_has_brand_and_size():
    '''has the brand and size passed to __init__, and values can be set to new instance.'''
    stan_smith = Shoe("Adidas", 9)
    assert(stan_smith.brand == "Adidas")
    assert(stan_smith.size == 9)

def test_requires_int_size():
    '''prints "size must be an integer" if size is not an integer.'''
    stan_smith = Shoe("Adidas", 9)
    captured_out = io.StringIO()
    sys.stdout = captured_out
    stan_smith.size = "not an integer"
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "size must be an integer\n"

def test_can_cobble():
    '''says that the shoe has been repaired.'''
    stan_smith = Shoe("Adidas", 9)
    captured_out = io.StringIO()
    sys.stdout = captured_out
    stan_smith.cobble()
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == "Your shoe is as good as new!\n")

def test_cobble_makes_new():
    '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
    stan_smith = Shoe("Adidas", 9)
    stan_smith.cobble()
    assert(stan_smith.condition == "New")

# Running the tests
test_has_brand_and_size()
test_requires_int_size()
test_can_cobble()
test_cobble_makes_new()

print("All tests passed.")
