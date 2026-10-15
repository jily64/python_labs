import json
from json import JSONDecodeError
import csv

# from src.lab04.io_txt_csv import read_text, write_csv


def check_headers(data: list[dict]):
    """
    Функция отвечает за проверку кол-ва колонок и их названий.
    """
    reference_keys = data[0].keys()
    for row in data:
        if row.keys() != reference_keys:
            raise ValueError("Ununified header values count or names")


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Конвертер json в csv.

    Открывает файл с json, читает его. Затем идут проверки (блок Checkers). Там мы проверяем данные на валидность.
    Затем через стандартный DictWriter в библиотеке csv записываю снова в файл.

    Отдельно ищу все поля, которые могу встретиться. Если в json отсутвует то или иное поле, то врайтер не упадет.

    Отдельно есть блок для обработки ошибок. Он ловит ошибку файл не найден и ошибку чтения json отдельно и выводит кастомные ValueError.
    Все остальные ошибки идут через последний блок, который просто рейзит ошибку
    """

    try:
        # Reader
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Checkers
        if not isinstance(data, list):
            raise TypeError("JSON file must have a list object")
        if not all([isinstance(i, dict) for i in data]):
            raise ValueError("There is no dicts in list")
        if len(data) == 0:
            raise ValueError("JSON must have 1 object at least")
        # check_headers(data) - dedicated

        # Writer
        all_keys = set()
        for row in data:
            all_keys.update(row.keys())

        headers = sorted(list(all_keys))
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(data)

    # Errors proceeder
    except FileNotFoundError as e:
        raise FileNotFoundError("Cant find file to read.")
    except JSONDecodeError as e:
        raise ValueError("Cant decode .json file")
    except Exception as e:
        raise e


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Открываем файл, определяем диалект по семплу из 2048 символов, проверем есть ли хеддер.
    Читаем данные через диктридер, передав в него определенный диалект.
    Отдельно проверяем, что данные (кол-во столбцов и их имена) совпадают.
    Записываем через json.dump

    Обработчик ошибок отлавливает только отсутствующий файл, а все остальные ошибки кидает напрямую.
    """

    try:
        # Reader
        with open(csv_path, "r", encoding="utf-8") as f:
            sample = f.read(2048)
            f.seek(0)

            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)

            # Header Checker
            if not sniffer.has_header(sample):
                raise ValueError(".csv must have headers")

            # Data Loader
            data = list(csv.DictReader(f, dialect=dialect))

        # Data and structure checkers
        if len(data) == 0:
            raise ValueError(".csv must have a least 1 data row")
        check_headers(data)

        # Writers
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # Errors proceeder
    except FileNotFoundError as e:
        raise FileNotFoundError("Cant find file to read.")
    except Exception as e:
        raise e


if __name__ == "__main__":
    sample_json = "data/samples/people.json"
    out_csv = "data/out/people_from_json.csv"
    out_json = "data/out/people_from_csv.json"

    print("=" * 60)

    try:
        # --------------------------------
        # JSON -> CSV
        # ---------------------------------
        print("Test 1: JSON -> CSV")
        with open(sample_json, "r", encoding="utf-8") as f:
            initial_json_len = len(json.load(f))

        json_to_csv(sample_json, out_csv)

        with open(out_csv, "r", encoding="utf-8") as f:
            resulting_csv_len = len(f.readlines()) - 1

        print(f" -> Zapisi JSON: {initial_json_len}")
        print(f" -> Zapisi CSV: {resulting_csv_len}")

        assert initial_json_len == resulting_csv_len, "Erorr"
        print(" Success")
        print("-" * 60)

        # --------------------------------
        # CSV -> JSON
        # --------------------------------
        print("Test 2: CSV -> JSON")
        csv_to_json(out_csv, out_json)

        with open(out_json, "r", encoding="utf-8") as f:
            final_json_len = len(json.load(f))

        print(f" -> Zapisi CSV: {resulting_csv_len}")
        print(f" -> Zapisi JSON: {final_json_len}")

        assert resulting_csv_len == final_json_len, "Erorr"
        print(" Success")
        print("=" * 60)

    except Exception as e:
        print(f"\nOh no! Erorr: {e}")
