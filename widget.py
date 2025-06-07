from datetime import datetime
from .masks import get_mask_card_number, get_mask_account


def mask_account_card(input_str: str) -> str:
    """Определяет тип данных (карта/счет) и применяет соответствующую маскировку"""
    if not input_str:
        return ""

    # Проверяем тип данных
    if "счет" in input_str.lower():
        # Ищем последовательность из 20+ цифр
        digits = ''.join(filter(str.isdigit, input_str))
        return get_mask_account(digits) if digits else ""

    else:  # Карта
        # Ищем последовательность из 16+ цифр
        digits = ''.join(filter(str.isdigit, input_str))
        return get_mask_card_number(digits) if digits else ""


def get_date(raw_date: str) -> str:
    """Преобразует дату из формата ISO в строку DD.MM.YYYY"""
    if not raw_date:
        return ""

    try:
        date_obj = datetime.fromisoformat(raw_date)
        return date_obj.strftime("%d.%m.%Y")
    except (TypeError, ValueError):
        return ""