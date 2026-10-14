from src.lib.text import top_n, tokenize, normalize, count_freq
from src.lib.tables import create_table
from src.lib.io_util import read_text_by_lines

import argparse
from pathlib import Path
        
def cat_command(input_file: str, n: bool = False):
    r"""
    Читаем файл по строкам (функция возвращает кортеж с номером строки и ее текстом).
    Просто выводим.
    
    Также я покрасил текст. Да, колораму поставть нельзя. поэтому просто воспользовался символами из ascii таблицы.
    
    \033[1m - жирный
    \033[34m - синий
    \033[0m - сброс
    """
    
    for line_num, line_text in read_text_by_lines(input_file):
        if n:
            print(f"\033[1m\033[34m{line_num+1}.\033[0m {line_text}")
            continue
        print(line_text)

def stats_command(input_file: str, top: int = 5):
    """
    Читаем файл по строкам, используя скользящий буфер для сохранения 
    целостности слов на стыках строк.
    """
    stats = {}
    buffer = ""
    final_char = ""

    for line_num, line_text in read_text_by_lines(input_file):
        if line_text.strip() == "":
            continue
        
        if buffer:
            if final_char == "-":
                combined_text = buffer + line_text
            else:
                combined_text = buffer + " " + line_text
        else:
            combined_text = line_text

        normalized_chunk = normalize(combined_text)
        tokens = tokenize(normalized_chunk)
        
        if not tokens:
            buffer = ""
            continue

        buffer = tokens[-1]
        final_char = line_text.strip()[-1]
        valid_tokens = tokens[:-1]

        freq = count_freq(valid_tokens)
        for key in freq:
            stats[key] = stats[key] + freq[key] if key in stats else freq[key]
            
    if buffer:
        final_token = tokenize(normalize(buffer))
        for key in final_token:
            stats[key] = stats[key] + 1 if key in stats else 1    
            
    print(create_table(("Слово", "Повторения"), top_n(stats, n=top))) # type: ignore
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")
    
    # подкоманда cat]
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Расположение файла")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Расположение файла")
    stats_parser.add_argument("--top", type=int, default=5, help="Обрезка топа")

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
        
    elif args.command == "stats":
        stats_command(args.input, args.top)