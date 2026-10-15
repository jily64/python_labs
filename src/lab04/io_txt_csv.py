from pathlib import Path
from src.lib.tables import check_rows


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
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


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Функция записывает .cvs файлики. От себя добавил создание папок, которых нет по пути.
    Сначало проверяет целостность данных, которые пришли нам на вход. Затем проверяет существует файл и
    является ли он файлом в принципе (чтобы не перезаписывать папку, что буквально невозможно).

    Потом просто создает недостающие папки на пути.

    Запись происходит в кодировке utf-8. Если есть заголовки, то сначало запишет их. Потом построчно соеденит все значения в каждом ряду через запятую.
    Ну и все впринципе.

    write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None
        rows: список строк (каждая строка - кортеж или список)
        path: путь к файлу (строка или объект Path)
        header: заголовок (кортеж строк) или None

    Ошибки:
        ValueError: если строки не соответствуют заголовку или содержат пустые строки
        ValueError: если путь не является файлом
    """
    p = Path(path)

    # Checkers
    if p.exists() and not p.is_file():
        raise ValueError(f"Path is not a file: {p}")
    if header is not None:
        check_rows(rows, header)
    else:
        check_rows(rows)

    # Creating dirs 42
    if not p.parent.exists():
        p.parent.mkdir(parents=True, exist_ok=True)

    # Write
    with p.open("w", encoding="utf-8") as f:
        if header is not None:
            f.write(",".join(header) + "\n")
        for row in rows:
            f.write(",".join(str(cell) for cell in row) + "\n")


if __name__ == "__main__":
    test_type = 0

    match test_type:
        case 0:
            write_csv([("word", "count"), ("test", 3)], "src/lab04/data/check.csv")
            print(read_text("src/lab04/data/check.csv"), "\n------------")

            write_csv(
                [("word", "count"), ("test", 3)],
                "src/lab04/data/check.csv",
                header=("word", "count"),
            )
            print(read_text("src/lab04/data/check.csv"), "\n------------")

            write_csv([], "src/lab04/data/check.csv", header=None)
            print(read_text("src/lab04/data/check.csv"), "\n------------")

            write_csv([], "src/lab04/data/check.csv", header=("word", "count"))
            print(read_text("src/lab04/data/check.csv"), "\n------------")

        case 1:
            print(read_text("src/lab04/data/check.csv"))
            print(read_text("src/lab04/data/check.csv", encoding="utf-8"))
