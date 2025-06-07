from datetime import datetime
from . import masks  # Измененный импорт


def mask_account_card(input_str: str) -> str:
    if not input_str:
        return ""

    if "счет" in input_str.lower():
        digits = ''.join(filter(str.isdigit, input_str))
        return masks.get_mask_account(digits) if digits else ""
    else:
        digits = ''.join(filter(str.isdigit, input_str))
        return masks.get_mask_card_number(digits) if digits else ""


def get_date(raw_date: str) -> str:
    if not raw_date:
        return ""

    try:
        date_obj = datetime.fromisoformat(raw_date)
        return date_obj.strftime("%d.%m.%Y")
    except (TypeError, ValueError):
        return ""
