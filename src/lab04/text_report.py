from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lib.tables import create_table, check_rows
from src.lab04.io_txt_csv import read_text, write_csv, check_rows

import sys, argparse
from multiprocessing import Process, Queue

KEYWORDS = ["--in", "--per-file", "--total", "--encoding"]


def args_parser(args: list[str]) -> dict[str, list[str]]:
    """
    Небольшой анвраппер аргументов. Есть список слов, которые он ищет. Все, что стоит после ключевых слов, записывает в словарик
    """
    res = {}
    previous_keyword = None

    for arg in args:
        if arg in KEYWORDS:
            if arg not in res:
                res[arg] = []
            previous_keyword = arg
            continue

        if not previous_keyword:
            continue

        res[previous_keyword].append(arg)

    return res


def report_for_each(files: list[str], output: str, texts: list[str], queue: Queue):
    """
    Функция считает топ слов по каждому файлу отдельно, записывает в .csv и генерит табличку.
    """

    # Process internal ID - 1
    try:
        results = []
        for text_ind in range(len(texts)):
            text_data = top_n(count_freq(tokenize(texts[text_ind])), n=-1)
            results += [
                [files[text_ind]] + list(text_data[i]) for i in range(len(text_data))
            ]
        queue.put((1, results))

    except Exception as e:
        queue.put((1, e))


def report_for_all(output: str, text: list[str], queue: Queue):
    """
    Функция считает топ слов по всем файлам, записывает в .csv и генерит табличку.

    Трай тут чисто для дебага, так как функция не может выдать ошибку как таковая
    """

    # Process internal ID - 2
    try:
        results = list(top_n(count_freq(tokenize("\n".join(text))), n=-1))
        queue.put((2, results))

    except Exception as e:
        queue.put((2, e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--in",
        nargs="+",
        required=True,
        dest="input_files",
        help="Список файлов",
    )
    parser.add_argument(
        "--per-file",
        default="src/lab04/data/reports/report_per_file.csv",
        help="Путь к отчету по каждому файлу",
    )
    parser.add_argument(
        "--total",
        default="src/lab04/data/reports/report_total.csv",
        help="Путь к общему отчету",
    )
    parser.add_argument(
        "--encoding", default="utf-8", help="Кодировка текстовых файлов"
    )

    args = parser.parse_args()

    per_file_out = args.per_file
    total_out = args.total

    text = []
    for file in args.input_files:
        text.append(
            normalize(read_text(path=file, encoding=args.encoding), casefold=True)
        )

    # Мне было нечем я заняться, поэтому я бахнул многопоток
    queue = Queue()

    each_process = Process(
        target=report_for_each,
        name="Report for each",
        args=[args.input_files, per_file_out, text, queue],
    )
    all_process = Process(
        target=report_for_all, name="Report for all", args=[total_out, text, queue]
    )

    each_process.start()
    all_process.start()

    each_process.join()
    all_process.join()

    data = {}
    for _ in range(2):
        proc_id, result = queue.get()
        data[proc_id] = result

    for proc_id, result in data.items():
        if isinstance(result, BaseException):
            print(f"Error in process with ID {proc_id}")
            raise result

        else:
            if proc_id == 1:
                write_csv(result, path=per_file_out, header=("file", "word", "count"))
                print(create_table(header=("file", "word", "count"), rows=result))

            elif proc_id == 2:
                write_csv(rows=result, path=total_out, header=("word", "count"))
                print(create_table(header=("word", "count"), rows=result))
