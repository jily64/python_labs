from pathlib import Path


def read_text_by_lines(path: str | Path, encoding: str = "utf-8"):
    """
    Функция читает файл построчно.
    
    read_text_by_lines(path: str | Path, encoding:str = "utf-8") -> str
        path: путь к файлу (строка или объект Path)
        encoding: кодировка файла (по умолчанию "utf-8")
        
    Ошибки:
        FileNotFoundError: если файл не найден
        ValueError: если путь не является файлом
    """
    path = Path(path)
    
    # Checkers
    if not path.exists():
        raise FileExistsError(f"Файл не найден: {path}")
    if not path.is_file():
        raise ValueError(f"Указанный путь не является файлом: {path}")
    
    with open(path, "r", encoding=encoding) as f:
        for line_number, line in enumerate(f, start=0):
            yield (line_number, line.strip())
            
def read_text(path: str | Path, encoding:str = "utf-8") -> str:
    """
    Проверяет существование файла, является ли путь файлом и возвращает его содержимое декдированное в строку.
    
    read_text(path: str | Path, encoding:str = "utf-8") -> str
        path: путь к файлу (строка или объект Path)
        encoding: кодировка файла (по умолчанию "utf-8")
        
    Ошибки:
        FileNotFoundError: если файл не найден
        ValueError: если путь не является файлом
        
    42 бро
    """
    p = Path(path)
    
    # Checkers
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    if not p.is_file():
        raise ValueError(f"Path is not a file: {p}")
    
    return p.read_text(encoding=encoding)