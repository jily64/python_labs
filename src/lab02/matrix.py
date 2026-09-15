"""
Код для задания B.
"""


from src.lib.matrix import matrix_rows_checkup, IrregularMatrixException


def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    """
    Переворачивает матрицу.
    
    Ошибки:
        ValueError: Неправильные размеры матрицы. (см. scr.lib.matrix)
    """
    if not matrix_rows_checkup(mat=mat):
        raise ValueError("Incorrect matrix")
    if not mat:
        return []

    a = [[] for _ in range(len(mat[0]))]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            a[j].append(mat[i][j])
    return a


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Возвращает сумму строк матрицы.
    
    Ошибки:
        ValueError: Неправильные размеры матрицы. (см. scr.lib.matrix)
    """
    if not matrix_rows_checkup(mat=mat):
        raise ValueError("Incorrect matrix")
    return [sum(i) for i in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Возвращает сумму столбцов матрицы.
    
    Ошибки:
        ValueError: Неправильные размеры матрицы. (см. scr.lib.matrix)
    """
    if not matrix_rows_checkup(mat=mat):
            raise ValueError("Incorrect matrix")
    return [sum(i) for i in transpose(mat)]


if __name__ == "__main__":
    """
    transpose_tests = [
        [[1, 2, 3]], 
        [[1], [2], [3]], 
        [[1, 2], [3, 4]],
        [], 
        [[1, 2], [3]]
    ]
        
    for i in transpose_tests:
        try:
            print(i, "->", transpose(i))
        except Exception as e:
            print(i, "->", e, f"Тип ошибки: {type(e)}")
    """
    
    """
    row_sums_tests = [
        [[1, 2, 3], [4, 5, 6]], 
        [[-1, 1], [10, -10]], 
        [[0, 0], [0, 0]],
        [[1, 2], [3]]
    ]
        
    for i in row_sums_tests:
        try:
            print(i, "->", row_sums(i))
        except Exception as e:
            print(i, "->", e, f"Тип ошибки: {type(e)}")
    """      
    
    """
    col_sums_tests = [
        [[1, 2, 3], [4, 5, 6]], 
        [[-1, 1], [10, -10]], 
        [[0, 0], [0, 0]],
        [[1, 2], [3]]
    ]
        
    for i in col_sums_tests:
        try:
            print(i, "->", col_sums(i))
        except Exception as e:
            print(i, "->", e, f"Тип ошибки: {type(e)}")
    """
    pass