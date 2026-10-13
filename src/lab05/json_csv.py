import json
from json import JSONDecodeError
import csv

# from src.lab04.io_txt_csv import read_text, write_csv


def check_headers(data: list[dict]):
    for i in range(len(data)-1):
        if len(data[i].keys()) != len(data[i+1].keys()):
            raise ValueError("Ununified header values count")

def json_to_csv(json_path: str, csv_path: str) -> None:
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
        check_headers(data)

        # Writer
        headers = data[0].keys()        
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, headers)
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
    pass


if __name__ == "__main__":
    json_to_csv("src/lab05/data/people.json", "src/lab05/data/people.csv")