from codigo.puzzle_001 import remove_letters



def test_get_only_digits():
    s = "one1two2three3four4five5six6seven7eight8nine9"
    expected = 19
    assert remove_letters(s) == expected