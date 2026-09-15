# Здесь собраны функции, которые могут быть использованы для работы с матрицами.


def matrix_rows_checkup(mat: list[list[float | int]]) -> bool:
    """    
    Делает проверку соответсвия длины строк в матрице.
    """
    if not mat:
        return True
    
    l = set([len(i) for i in mat])
    return len(l) == 1


# Здесь собраны остальные объекты, которые тоже относятся к матрицам.


class IrregularMatrixException(Exception):
    """
    Exception с подписью об ошибке в строении матрицы.
    """
    
    def __init__(self, *args: object) -> None:
        self.add_note("Irregular Matrix")
        super().__init__(*args)