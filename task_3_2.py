import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа, які відокремлені пробілами у тексті.

    :param text: Вхідний текст для аналізу
    :return: Генератор дійсних чисел
    """
    pattern = r'(?<=\\s)(\\d+\\.\\d+)(?=\\s)'
    for match in re.finditer(pattern, text):
        yield float(match.group(1))

def sum_profit(text: str, func: Callable) -> float:
    """
    Підсумовує всі дійсні числа, знайдені у тексті за допомогою генератора.

    :param text: Вхідний текст для аналізу
    :param func: Функція-генератор для пошуку чисел
    :return: Сума всіх знайдених чисел
    """
    return sum(func(text))
