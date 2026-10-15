import pytest
from src.lib.json_csv import json_to_csv, csv_to_json

import json, csv, openpyxl
from pathlib import Path

@pytest.fixture
def tmp_path():
    return "./tests/data/"

def test_json_to_csv_roundtrip(tmp_path: Path):
    src = Path(tmp_path + "people.json")
    dst = Path(tmp_path + "people_from_json.csv")
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

def test_csv_to_json_roundtrip(tmp_path: Path):
    src = Path(tmp_path + "people.csv")
    dst = Path(tmp_path + "people_from_csv.json")
    data = '''
    name,age
    alice,22
    bob,25
    '''


    src.write_text(data, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = json.load(f)

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    # TODO: Реализовать тесты для конвертации в другую сторону
    pass


# Бро я придумал свои тесты
# и тд....
