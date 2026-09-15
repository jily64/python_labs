def fio_string_unwrapper(fio: str) -> list[str]:    
    """
    Просто превращает строку с фио в адекватный вид и возвращает ее раздеренной на слова.
    """
    
    return [i[0].upper() + i[1:] for i in fio.split()]

def check_fio(fio: str) -> bool:
    """
    Проверка фио на ошибки.
    """
    
    splitted_fio = fio.strip().split()
    if len(splitted_fio) < 2 or len(splitted_fio) > 3:
        return False
    return True

def check_group(group: str) -> bool:
    """
    Проверка группы на ошибки.
    """
    
    if len(group.strip()) == 0:
        return False
    return True

def format_record(rec: tuple[str, str, float]) -> str:
    """
        rec: tuple[fio: str, group: str, gpa: float] -> str
        
        Функция форматирования данных студента (или кого то еще) в строку вида:
        
        "Фамилия И. О., гр. ГРУППА, GPA .2f"    
    """
    
    # Checkers
    if not check_fio(rec[0]):
        raise ValueError("Incorrect FIO string. Minimal word count - 2. Maximum word count - 3.")
    if not check_group(rec[1]):
        raise ValueError("Incorrect Group string. String length cant be less that 1 char.")
    
    # Formatting
    unwrapped_fio = fio_string_unwrapper(rec[0])
    final_fio = unwrapped_fio[0]+" "+". ".join([unwrapped_fio[i][0] for i in range(1, len(unwrapped_fio))])+"."
    
    return f"{final_fio}, гр. {rec[1].strip().upper()}, GPA {rec[2]:.2f}"


if __name__ == "__main__":
    format_record_tests = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6), 
        ("Петров Пётр", "IKBO-12", 5.0), 
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
        ("       ", "BIVT", 123.001),
        ("Олег Олегович Монгол", "    ", 123.001),
    ]
        
    for i in format_record_tests:
        try:
            print(i, "->", format_record(i))
        except Exception as e:
            print(i, "->", e, f"Тип ошибки: {type(e)}")
