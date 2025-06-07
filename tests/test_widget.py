import pytest

from PythonProject.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Счет 73654108430135874305") == "**4305"
    assert mask_account_card("Visa Platinum 7000792163956361") == "7000 79** **** 6361"
