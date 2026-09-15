# Здесь собраны функции, которые могут быть использованы для работы с матрицами.


def matrix_rows_checkup(mat: list[list[float | int]]) -> bool:
    """    
    Делает проверку соответсвия длины строк в матрице.
    """
    
    a = set([len(i) for i in mat])
    if len(a) > 1:
        return False
    return True


# Здесь собраны остальные объекты, которые тоже относятся к матрицам.


class IrregularMatrixException(Exception):
    """
    Exception с подписью об ошибке в строении матрицы.
    """
    
    def __init__(self, *args: object) -> None:
        self.add_note("Irregular Matrix")
        super().__init__(*args)