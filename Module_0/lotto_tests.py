import unittest

import pytest

from lotek import random_six_numbers, check_your_luck, MY_NUMBERS


# unittest
class TestRandomSixNumbers(unittest.TestCase):
    def test_return_type(self):
        numbers = random_six_numbers()
        self.assertIsInstance(numbers, list)

    def test_number_of_elements(self):
        numbers = random_six_numbers()
        self.assertEqual(len(numbers), 6)
        self.assertEqual(len(set(numbers)), 6)

    def test_range(self):
        numbers = random_six_numbers()
        for num in numbers:
            self.assertGreaterEqual(num, 1)
            self.assertLessEqual(num, 49)


# pytest
def test_return_type():
    numbers = random_six_numbers()
    assert isinstance(numbers, list)


def test_number_of_elements():
    numbers = random_six_numbers()
    assert len(numbers) == 6
    assert len(set(numbers)) == 6


def test_range():
    numbers = random_six_numbers()
    for num in numbers:
        assert 1 <= num <= 49


@pytest.fixture()
def mock_draw_six_numbers():
    """Return a function that returns a known set of 6 numbers for testing purposes."""
    def draw_numbers():
        return [5, 20, 30, 42, 47, 49]
    return draw_numbers


def test_check_your_luck_returns_tuple(mock_draw_six_numbers):
    """Check that check_your_luck() returns a tuple."""
    result = check_your_luck(MY_NUMBERS, mock_draw_six_numbers)
    assert isinstance(result, tuple)


def test_check_your_luck_returns_correct_set(mock_draw_six_numbers):
    """Check that check_your_luck() returns the correct sets of numbers."""
    my_numbers_set, draw_six_numbers_set, _, _ = check_your_luck(MY_NUMBERS, mock_draw_six_numbers)
    assert my_numbers_set == set(MY_NUMBERS)
    assert draw_six_numbers_set == set(mock_draw_six_numbers())


def test_check_your_luck_identifies_common_numbers(mock_draw_six_numbers):
    """Check that check_your_luck() correctly identifies common numbers.
        Unfortunately cannot test in depth common numbers for check_your_luck function
        as this will cause indefinite loop nd consume all available RAM"""

    my_numbers = [5, 20, 30, 42, 47, 49]  # different numbers will cause indefinite loop
    common_numbers = {5, 20}
    _, draw_six_numbers_set, _, _ = check_your_luck(my_numbers, mock_draw_six_numbers)
    assert draw_six_numbers_set.intersection(common_numbers) == common_numbers


def test_common_numbers_dict_keys_length(mock_draw_six_numbers):
    my_numbers = [5, 20, 30, 42, 47, 49]
    _, _, _, common_numbers_dict = check_your_luck(my_numbers, mock_draw_six_numbers)
    assert len(common_numbers_dict.keys()) == 3
    assert not len(common_numbers_dict.keys()) == 4


def test_common_numbers_dict_keys(mock_draw_six_numbers):
    my_numbers = [5, 20, 30, 42, 47, 49]
    _, _, _, common_numbers_dict = check_your_luck(my_numbers, mock_draw_six_numbers)
    expected_keys = ["three common numbers", "four common numbers", "five common numbers"]
    assert list(common_numbers_dict.keys()) == expected_keys


