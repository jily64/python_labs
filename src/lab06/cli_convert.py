import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

from pathlib import Path

if __name__ == "__main__":
    """
    Тут толком описывать нечего
    """

    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help="Input file direction")
    p1.add_argument("--out", dest="output", required=True, help="Output file direction")

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help="Input file direction")
    p2.add_argument("--out", dest="output", required=True, help="Output file direction")

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Input file direction")
    p3.add_argument("--out", dest="output", required=True, help="Output file direction")

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
    if args.command == "csv2json":
        csv_to_json(args.input, args.output)
    if args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

    print(f"Converted successfully!\nOutput: {Path(args.output).absolute()}")
