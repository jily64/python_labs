"""
Код для задания номер 1.
"""


def _min_max_old(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Возвращает кортеж из минимального и максимального.
    
    Ошибки:
        ValueError: Если список пуст.
    """
    if not nums:
        raise ValueError("Array must have at least 1 element")
    return (min(nums), max(nums))


def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
        Возвращает кортеж из минимального и максимального.
        
        Ошибки:
            ValueError: Если список пуст.
    """
    if not nums:
        raise ValueError("Array must have at least 1 element")

    n_min = 2**31
    n_max = -(2**31)

    for i in nums:
        if i > n_max:
            n_max = i
        if i < n_min:
            n_min = i

    return (n_min, n_max)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает список отсортированных, уникальных значений
    """
    num_set = list(set(nums))

    for i in range(len(num_set)):
        for j in range(len(num_set) - 1 - i):
            if num_set[j] > num_set[j + 1]:
                num_set[j], num_set[j + 1] = num_set[j + 1], num_set[j]

    return num_set


def flatten(mat: list[list | tuple]) -> list:
    """
    Раскрывает вложенные списки и кортежи и превращает все это дело в 1 список.
    
    Ошибки:
        TypeError: Элементами входного списка могут быть только кортеж и список.
    """
    
    a = []
    for i in mat:
        if not isinstance(i, tuple) and not isinstance(i, list):
            raise TypeError("Matrix elements must be type of tuple or list.")
        a.extend(i)
    return a


"""
    Сделанно просто так. Не обращайте внимания.
"""
def flatten_v2(mat: list[list | tuple | int | float]) -> list[float | int]:
    a = []
    for i in mat:
        data = i
        if isinstance(i, (list, tuple)):
            data = flatten_v2(list(i))
            a += data
            continue
        
        if not isinstance(i, (list, tuple)):
            raise TypeError("Array elements must be type of int or float.")
        
        a.append(i)
        
    return a

if __name__ == "__main__":
    """
    min_max_tests = [
        [3, -1, 5, 5, 0], 
        [-5, -2, -9], 
        [], 
        [1.5, 2, 2.0, -3.1]
    ]
    
    for i in min_max_tests:
        try:
            print(i, "->", min_max(i))
        except Exception as e:
            print(i, "->", e, f"Тип ошибки: {type(e)}")
    """
    
    
    unique_sorted_tests = [
        [3, 1, 2, 1, 3],  
        [], 
        [-1, -1, 0, 2, 2],
        [1.0, 1, 2.5, 2.5, 0]
    ]
        
    for i in unique_sorted_tests:
        try:
            print(i, "->", unique_sorted(i))
        except Exception as e:
            print(i, "->", e, f"Тип ошибки: {type(e)}")
    
    
    """
    flatten_tests = [
        [[1, 2], [3, 4]],  
        [[1, 2], (3, 4, 5)], 
        [[1], [], [2, 3]],
        [[1, 2], "ab"]
    ]
            
    for i in flatten_tests:
        try:
            print(i, "->", flatten(i))
        except Exception as e:
            print(i, "->", e, f"Тип ошибки: {type(e)}")
    """
    pass