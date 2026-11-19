import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lib.tables import create_table

REPO_ROOT = Path(__file__).resolve().parents[2]
BENCH_CSV = REPO_ROOT / "data" / "lab07" / "bench.csv"

HEADER = ("task", "n", "impl", "seconds")

SORT_SIZES = (1_000, 10_000, 100_000)
SEARCH_N = 100_000
SEARCH_QUERIES = 10_000
TWO_SUM_SIZES = (1_000, 10_000)

# На 10^5 квадратичные сортировки честно считать полчаса, поэтому
# по ТЗ разрешено поставить ">60" и не мучить ноутпук.
SORT_TIME_LIMIT = 60


def make_numbers(n: int) -> list[int]:
    """Одни и те же данные для всех алгоритмов (random.seed(42) в main)."""
    return [random.randint(-1_000_000, 1_000_000) for _ in range(n)]


def measure(fn) -> float:
    """Один запуск через timeit, как в теории."""
    return timeit.timeit(fn, number=1)


def bench_sorts() -> list[tuple]:
    """
    sorted против трех своих сортировок на одинаковых данных.
    На 10^5 для квадратичных считаем оценку по замеру на 10^4:
    рост n в 10 раз => рост времени примерно в 100 раз.
    """
    rows = []
    timings = {}

    for n in SORT_SIZES:
        data = make_numbers(n)

        seconds = measure(lambda: sorted(data))
        rows.append(("sort", n, "sorted", round(seconds, 6)))

        for name, fn in (
            ("bubble", bubble_sort),
            ("insertion", insertion_sort),
            ("selection", selection_sort),
        ):
            if n == 100_000 and timings[(name, 10_000)] * 100 > SORT_TIME_LIMIT:
                rows.append(("sort", n, name, ">60"))
                continue

            seconds = measure(lambda: fn(data))
            timings[(name, n)] = seconds
            rows.append(("sort", n, name, round(seconds, 6)))

    return rows


def bench_search() -> list[tuple]:
    """
    Линейный и бинарный поиск на одном списке из 100 000 чисел,
    по 10 000 случайных запросов (все значения точно есть в списке).
    Для бинарного отдельной строкой пишем время сортировки,
    потому что без нее он работать не умеет.
    """
    rows = []

    data = make_numbers(SEARCH_N)
    queries = [random.choice(data) for _ in range(SEARCH_QUERIES)]

    seconds = measure(lambda: [linear_search(data, x) for x in queries])
    rows.append(("search", SEARCH_N, "linear", round(seconds, 6)))

    seconds = measure(lambda: sorted(data))
    rows.append(("search", SEARCH_N, "sort_for_binary", round(seconds, 6)))

    sorted_data = sorted(data)
    seconds = measure(lambda: [binary_search(sorted_data, x) for x in queries])
    rows.append(("search", SEARCH_N, "binary", round(seconds, 6)))

    return rows


def bench_two_sum() -> list[tuple]:
    """
    Брутфорс против словаря. target собираем из последней пары, поэтому
    брутфорсу приходится перебрать почти все пары, а не найти ответ сразу.
    Данные берем из широкого диапазона, чтобы лишних пар-совпадений не было.
    """
    rows = []

    for n in TWO_SUM_SIZES:
        data = [random.randint(-10**12, 10**12) for _ in range(n)]
        target = data[-1] + data[-2]

        seconds = measure(lambda: two_sum_brute(data, target))
        rows.append(("two_sum", n, "brute", round(seconds, 6)))

        seconds = measure(lambda: two_sum_fast(data, target))
        rows.append(("two_sum", n, "fast", round(seconds, 6)))

    return rows


if __name__ == "__main__":
    random.seed(42)

    rows = []
    rows += bench_sorts()
    rows += bench_search()
    rows += bench_two_sum()

    print(create_table(HEADER, rows))
    write_csv(rows, BENCH_CSV, header=HEADER)
    print(f"CSV сохранён: {BENCH_CSV}")
