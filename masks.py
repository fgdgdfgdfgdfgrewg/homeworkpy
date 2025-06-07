def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя первые 4 и последние 4 цифры"""
    if not card_number or len(card_number) < 12:
        return "Некорректный номер карты"

    # Удаляем все пробелы и нецифровые символы
    cleaned = ''.join(filter(str.isdigit, card_number))

    if len(cleaned) < 12:
        return "Некорректный номер карты"

    return f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"


def get_mask_account(account: str) -> str:
    """Маскирует номер счета, оставляя только последние 4 цифры"""
    if not account or len(account) < 4:
        return "Некорректный номер счета"

    # Удаляем все пробелы и нецифровые символы
    cleaned = ''.join(filter(str.isdigit, account))

    if len(cleaned) < 4:
        return "Некорректный номер счета"

    return f"**{cleaned[-4:]}"