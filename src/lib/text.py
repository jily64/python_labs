import re, unicodedata


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Функция для нормализации текста. Первые 2 ифа переводят текст (в зависимости от выбраного метода) и меняет ё на е.
    
    Дальше, с помощью регулярки, заменяем все управляющие символы на пробелы. (в юникоде с x00 по x1F включительно и отдельно симвод x7F который отвечает за уделение символа)
    
    Обработки ошибок у функции не предсмотренно
    
    normalize(text: str, *, casefold: bool = False, yo2e: bool = True) -> str
    
    """
    
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    
    if yo2e:
        text = re.sub(r"[ёЁ]", "е", text)
    
    return " ".join(re.sub(r"[\x00-\x1F\x7F]", " ", text).split())

def tokenize(text: str) -> list[str]:
    """
    здесь тоже очень просто.
    
    При помощи регулярки и функции finall ищем либо полностью слова, либо слова с дефисами, после которых обязательно идет еще слово. Ну и так пока не закончится трока (* в конце паттерна)
    
    Обработки ошибок у функции не предсмотренно
    
    tokenize(text: str) -> list[str]    
    """
    
    return re.findall(r"\w+(?:-\w+)*", text, flags=re.UNICODE)

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Функция подсчета частоты слов в списке токенов.
    
    Просто бежит по списку и записывает все слова в словарь и потом его возвращает.
    
    Обработки ошибок у функции не предсмотренно
    
    count_freq(tokens: list[str]) -> dict[str, int]
    """
    
    freq_dict = {}
    
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Функция возвращает топ n слов по частоте встречаемости в виде списка кортежей (слово, частота)
    
    Сортировка идет по убыванию частоты, а при равной частоте - по алфавиту.
    При помощи безымянной функции сортируем словарь по значениям и ключам и возвращаем первые N элементов. 
    Минус у значения в сортировке нужен для того чтобы сортировка шла по убыванию, а не по возрастанию.
    
    Обработки ошибок у функции не предсмотренно
    
    top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]
    """
    
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]


if __name__ == "__main__":
    test_index = 2
    
    match test_index:
        case 0:
            normalize_tests = [
                ("ПрИвЕт\nМИр\t", False, True), 
                ("ёжик, Ёлка", True, True), 
                ("Hello\r\nWorld", False, False),
                ("  двойные   пробелы  ", True, False),
                ("  Привет, как дела?  ", False, False),
            ]
                
            for i in normalize_tests:
                print(normalize(i[0], casefold=i[1], yo2e=i[2]))
        
        case 1:
            tokenize_tests = [
                ("привет мир"),
                ("hello,world!!!"),
                ("по-настоящему круто"),
                ("2025 год"),
                ("emoji 😀 не слово"),
            ]
            
            for i in tokenize_tests:
                print(tokenize(i))

        case 2:
            count_freq_tests = [
                ["a","b","a","c","b","a"],
                ["bb","aa","bb","aa","cc"],
            ]
            
            for i in count_freq_tests:
                print(f"count_freq({i}) = {count_freq(i)}\ntop_n(count_freq({i}), 2) = {top_n(count_freq(i), 2)}\n")
    