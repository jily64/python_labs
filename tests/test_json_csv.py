import pytest
from src.lib.json_csv import json_to_csv, csv_to_json

import json, csv, openpyxl


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())

    print("Test 1: JSON -> CSV")
    with open(src, "r", encoding="utf-8") as f:
        initial_json_len = len(json.load(f))

    json_to_csv(src, dst)

    with open(dst, "r", encoding="utf-8") as f:
        resulting_csv_len = len(f.readlines()) - 1

    print(f" -> Zapisi JSON: {initial_json_len}")
    print(f" -> Zapisi CSV: {resulting_csv_len}")

    assert initial_json_len == resulting_csv_len, "Erorr"
    print(" Success")
    print("-" * 60)


def test_csv_to_json_roundtrip(tmp_path: Path):
    # TODO: Реализовать тесты для конвертации в другую сторону
    pass


# Бро я придумал свои тесты
# и тд....
