def linear_search(nums, x) -> int:
    """
    Просто идем по списку слева направо и возвращаем индекс первого вхождения.
    Если не нашли - возвращаем -1.

    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums, x) -> int:
    """
    Классика с двумя границами: lo и hi. Смотрим в середину, сравниваем
    и отбрасываем половину, в которой числа точно не может быть.

    ВАЖНО: список должен быть отсортирован по возрастанию.
    На неотсортированном списке результат не определён.

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        middle = (lo + hi) // 2

        if x < sorted_nums[middle]:
            hi = middle - 1
        elif x > sorted_nums[middle]:
            lo = middle + 1
        else:
            return middle

    return -1


def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """
    Брутальный перебор пар, йоуу. Два вложенных цикла, зато без словарей
    и вообще без мозгов.

    Возвращаем пару индексов (i, j), где i < j, или None.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """
    Он не такой брутальный, но зато быстрый и со словарем.
    Идем один раз по списку и запоминаем "значение -> индекс".
    Для каждого числа проверяем, видели ли мы уже target - nums[i].

    При нескольких ответах может вернуть любую подходящую пару.
    """
    seen = {}
    for i in range(len(nums)):
        dif = target - nums[i]
        if dif in seen:
            return (seen[dif], i)
        seen[nums[i]] = i
    return None


if __name__ == "__main__":
    assert linear_search([4, 2, 7, 2], 2) == 1
    assert linear_search([4, 2, 7, 2], 9) == -1
    assert binary_search([1, 3, 5, 7], 5) == 2
    assert binary_search([1, 3, 5, 7], 4) == -1
    assert two_sum_brute([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_fast([2, 7, 11, 15], 9) == (0, 1)
    print("search.py: OK")
