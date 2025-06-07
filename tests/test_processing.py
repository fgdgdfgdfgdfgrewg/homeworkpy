import pytest

from PythonProject.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_operations):
    filtered = filter_by_state(sample_operations, "EXECUTED")
    assert all(op["state"] == "EXECUTED" for op in filtered)

    canceled = filter_by_state(sample_operations, "CANCELED")
    assert len(canceled) == 1


@pytest.mark.parametrize("reverse, expected_order", [
    (True, [3, 1, 2]),
    (False, [2, 1, 3]),
])
def test_sort_by_date(sample_operations, reverse, expected_order):
    sorted_ops = sort_by_date(sample_operations, reverse)
    assert [op["id"] for op in sorted_ops] == expected_order
