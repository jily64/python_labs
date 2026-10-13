import csv
import openpyxl
from src.lib.tables import check_rows

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        # xlsx converter setup
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Reader
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)

        #Checkers
        if len(rows) <= 1:
            raise ValueError("Not enough values in .csv. File must have at least 2 rows (Header + 1 data row)")
        check_rows(rows)

        # Writer
        for row in rows:
            ws.append(row)
        wb.save(xlsx_path)

    # Errors proceeder
    except FileNotFoundError as e:
        raise FileNotFoundError("Cant find file to read.")
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    csv_to_xlsx("src/lab05/data/people.csv", "src/lab05/data/people.xlsx")
    