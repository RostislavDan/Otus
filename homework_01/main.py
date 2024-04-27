"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def filter_numbers(list_of_numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == "odd":
        return list(filter(lambda num: num % 2, list_of_numbers))
    elif filter_type == "even":
        return list(filter(lambda num: num % 2 == 0, list_of_numbers))
    else:
        return list(filter(is_prime, list_of_numbers))
