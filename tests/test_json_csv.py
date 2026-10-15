import pytest
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

import json, csv, openpyxl
from pathlib import Path


def test_json_to_csv_roundtrip(tmp_path):
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


def test_csv_to_json_roundtrip(tmp_path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = "name,age\nalice,22\nbob,25"

    src.write_text(data, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = json.load(f)

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_xlsx_roundtrip(tmp_path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.xlsx"
    data = "name,age\nalice,22\nbob,25"

    src.write_text(data, encoding="utf-8")

    csv_to_xlsx(str(src), str(dst))

    wb = openpyxl.load_workbook(dst)
    ws = wb["Sheet1"]
    final_xlsx_len = ws.max_row - 1

    assert final_xlsx_len == 2
    assert {"name", "age"} <= set([cell.value for cell in ws[1]])


#   Бро я придумал свои тесты
#   и тд....
