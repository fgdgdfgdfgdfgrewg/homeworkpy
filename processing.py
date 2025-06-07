from datetime import datetime
from typing import Dict, List, Literal


def filter_by_state(
        operations: List[Dict],
        state: Literal["EXECUTED", "CANCELED", "PENDING"]
) -> List[Dict]:
    """Фильтрует операции по статусу"""
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
        operations: List[Dict],
        reverse: bool = True
) -> List[Dict]:
    """Сортирует операции по дате (по умолчанию - от новых к старым)"""

    def get_date(op):
        date_str = op.get("date", "")
        try:
            return datetime.fromisoformat(date_str)
        except (TypeError, ValueError):
            return datetime.min

    return sorted(
        operations,
        key=get_date,
        reverse=reverse
    )