import pytest


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15T12:30:45.123456"},
        {"id": 2, "state": "CANCELED", "date": "2022-05-20T18:15:00.654321"},
        {"id": 3, "state": "EXECUTED", "date": "2023-03-10T08:45:33.987654"},
    ]
