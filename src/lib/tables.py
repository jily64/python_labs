def check_rows(rows: list[tuple | list], header: tuple[str, ...] | None = None) -> None:
    """
    Проверяет строки на соответствие заголовку и на наличие пустых строк.

    check_rows(rows: list[tuple | list], header: tuple[str, ...] | None = None) -> None
        rows: список строк (каждая строка - кортеж или список)
        header: заголовок (кортеж строк) или None

    Ошибки:
        ValueError: если строки не соответствуют заголовку или содержат пустые строки
    """
    if header is not None:
        for row in rows:
            if len(row) != len(header):
                raise ValueError(
                    f"Row length {len(row)} does not match header length {len(header)}"
                )
    else:
        for row in rows:
            if any(cell == "" for cell in row):
                raise ValueError(f"Row contains empty cell: {row}")


def create_table(header: tuple[str, ...], rows: list[tuple | list]):
    check_rows(header=header, rows=rows)

    result = ""

    for_each_col_length = []
    for col_num in range(len(header)):
        for_each_col_length.append(
            max(len(header[col_num]), max(len(str(row[col_num])) for row in rows))
        )

    result += (
        "┌"
        + "┬".join(
            [
                f"─" * (for_each_col_length[col_num] + 2)
                for col_num in range(len(header))
            ]
        )
        + "─┐\n"
    )
    result += (
        "│ "
        + " │ ".join(
            [
                f"{header[col_num]:<{for_each_col_length[col_num]}}"
                for col_num in range(len(header))
            ]
        )
        + "  │\n"
    )
    result += (
        "├"
        + "┼".join(
            [
                f"─" * (for_each_col_length[col_num] + 2)
                for col_num in range(len(header))
            ]
        )
        + "─┤\n"
    )
    for row in rows:
        result += (
            "│ "
            + " │ ".join(
                [
                    f"{row[col_num]:<{for_each_col_length[col_num]}}"
                    for col_num in range(len(row))
                ]
            )
            + "  │\n"
        )
    result += (
        "└"
        + "┴".join(
            [
                f"─" * (for_each_col_length[col_num] + 2)
                for col_num in range(len(header))
            ]
        )
        + "─┘\n"
    )

    return result
