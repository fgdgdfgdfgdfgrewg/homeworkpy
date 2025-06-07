import pytest

from PythonProject.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_num, expected", [
    ("7000792163956361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("", "Некорректный номер карты"),
    ("1234", "Некорректный номер карты"),
])
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize("account, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678901234567890", "**7890"),
    ("", "Некорректный номер счета"),
    ("123", "Некорректный номер счета"),
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
