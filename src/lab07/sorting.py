def bubble_sort(nums: list[int | float]) -> list[int | float]:
    """
    Алиса, пузырики.

    Бежим внешним циклом по чиселкам, внутренним сравниваем две пары чиселок.
    Если первое больше второго, то меняем их местами.
    Если за проход ничего не поменялось, ломаемся и возвращаем список.

    Возвращаем НОВЫЙ список, исходный не трогаем.
    """
    nums = list(nums)
    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break

    return nums


def insertion_sort(nums: list[int | float]) -> list[int | float]:
    """
    Берем число и просто двигаем его влево, пока слева число будет больше.
    Когда нашли место - вставляем.

    Возвращаем НОВЫЙ список, исходный не трогаем.
    """
    nums = list(nums)

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


def selection_sort(nums: list[int | float]) -> list[int | float]:
    """
    Находим минимальный элемент в неотсортированной части списка
    и меняем его местами с первым элементом этой части.

    Возвращаем НОВЫЙ список, исходный не трогаем.
    """
    nums = list(nums)
    n = len(nums)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == "__main__":
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert insertion_sort([3, 1, 2]) == [1, 2, 3]
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert insertion_sort([5]) == [5]
    assert selection_sort([2, 2, 1]) == [1, 2, 2]
    print("sorting.py: OK")
