def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not len(nums):
        raise ValueError("Array must have at least 1 element")
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(sorted(set(nums)))

# То, что надо сделать по ТЗ
def flatten(mat: list[list | tuple]) -> list:
    a = []
    for i in mat:
        if not isinstance(i, tuple) and not isinstance(i, list):
            raise TypeError("Matrix elements must be type of tuple or list.")
        a+=i
    return a


"""
    Сделанно просто так. Не обращайте внимания.
"""
def flatten_v2(mat: list[list | tuple | int | float]) -> list[float | int]:
    a = []
    for i in mat:
        data = i
        if isinstance(i, list) or isinstance(i, tuple):
            data = flatten_v2(list(i))
            a += data
            continue
        
        if not isinstance(i, int) and not isinstance(i, float):
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