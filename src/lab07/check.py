import random

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
) # Гыг, увидел в тиктоке что так можно делать
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> int:
    """
    Гоняем сортировку на случайных списках и сравниваем с эталоном sorted.
    Заодно проверяем, что исходный список не изменился.

    Списки разной длины: от пустого до 50 элементов, значения от -100 до 100,
    повторы тоже попадаются.
    """
    checks = 0

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        result = fn(nums)

        assert result == sorted(nums), (
            f"{fn.__name__} ошиблась на {original}: получилось {result}"
        )
        assert nums == original, (
            f"{fn.__name__} изменила исходный список: было {original}, стало {nums}"
        )
        checks += 2

    return checks


def check_search(trials: int = 100) -> int:
    """
    linear_search сравниваем с list.index (и -1 против ValueError).
    binary_search проверяем на отсортированных списках: он может вернуть
    любой индекс, поэтому смотрим, что на этом месте действительно лежит x.
    Отдельно прогоняем крайние случаи: пустой список, один элемент,
    первый/последний элемент и отсутствующее значение.
    """
    checks = 0

    edge_cases = [
        ([], 5),
        ([5], 5),
        ([5], 4),
        ([1, 2], 1),
        ([1, 2], 2),
        ([1, 2], 3),
    ]

    for nums, x in edge_cases:
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1

        got_linear = linear_search(nums, x)
        assert got_linear == expected, (
            f"linear_search не нашёл крайний случай: {nums}, x={x}: "
            f"получилось {got_linear}, ожидалось {expected}"
        )

        got_binary = binary_search(nums, x)
        assert got_binary == expected, (
            f"binary_search не нашёл крайний случай: {nums}, x={x}: "
            f"получилось {got_binary}, ожидалось {expected}"
        )
        checks += 2

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)

        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1

        got_linear = linear_search(nums, x)
        assert got_linear == expected, (
            f"linear_search разошёлся с list.index на {nums}, x={x}: "
            f"получилось {got_linear}, ожидалось {expected}"
        )
        checks += 1

        sorted_nums = sorted(nums)
        got_binary = binary_search(sorted_nums, x)
        if x in sorted_nums:
            assert got_binary != -1 and sorted_nums[got_binary] == x, (
                f"binary_search не нашёл {x} в {sorted_nums}: "
                f"получилось {got_binary}"
            )
        else:
            assert got_binary == -1, (
                f"binary_search нашёл несуществующий {x} в {sorted_nums}: "
                f"получилось {got_binary}"
            )
        checks += 1

    return checks


def check_two_sum(trials: int = 100) -> int:
    """
    Оба решения должны либо оба вернуть None, либо оба вернуть валидную пару.
    Пары могут быть разными (при нескольких ответах это нормально),
    поэтому проверяем сумму и порядок индексов, а не равенство ответов.
    """
    checks = 0

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        assert (brute is None) == (fast is None), (
            f"two_sum разошлись на {nums}, target={target}: "
            f"brute={brute}, fast={fast}"
        )
        checks += 1

        if brute is not None:
            i, j = brute
            assert i < j and nums[i] + nums[j] == target, (
                f"two_sum_brute вернул неправильную пару {brute} "
                f"для {nums}, target={target}"
            )
            checks += 1

            fi, fj = fast
            assert fi < fj and nums[fi] + nums[fj] == target, (
                f"two_sum_fast вернул неправильную пару {fast} "
                f"для {nums}, target={target}"
            )
            checks += 1

    return checks


if __name__ == "__main__":
    random.seed(42)

    total = 0
    for sort_fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(sort_fn)
    total += check_search()
    total += check_two_sum()

    print(f"OK: {total} проверок")
