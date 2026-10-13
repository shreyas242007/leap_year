from leap_year import is_leap_year

def test_leap_year_divisible_by_4():
    assert is_leap_year(2024) == True

def test_leap_year_century_not_leap():
    assert is_leap_year(1900) == False

def test_leap_year_century_is_leap():
    assert is_leap_year(2000) == True

def test_leap_year_regular():
    assert is_leap_year(2023) == False