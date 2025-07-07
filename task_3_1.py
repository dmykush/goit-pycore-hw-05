def caching_fibonacci():
    """
    Повертає функцію fibonacci(n), яка обчислює n-те число Фібоначчі
    з використанням кешування результатів у словнику cache.
    """
    cache = {}  # Словник для кешування обчислених значень

    def fibonacci(n):
        """
        Рекурсивно обчислює n-те число Фібоначчі з кешуванням.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        # Обчислення і збереження у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
