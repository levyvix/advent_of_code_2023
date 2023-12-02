from codigo.puzzle_002 import get_digits

def test_start_letter_end_letter():
    assert get_digits("two4nineeightseven41231232two") == 22


def test_start_letter_end_number():
    assert get_digits("nine6vjxjvmzpqtwonineseven8") == 98


def test_start_number_end_letter():
    assert get_digits("six7jr") == 67


def test_eightwo():
    assert get_digits("eightwo") == 82


def test_nineight():
    assert get_digits("nineight") == 98
