# ЛР07

# FastTravel
1. [search.py](#searchpy)
    - [linear_search](#linear_search)
    - [binary_search](#binary_search)
    - [two_sum_brute](#two_sum_brute)
    - [two_sum_fast](#two_sum_fast)
2. [sorting.py](#sortingpy)
    - [bubble_sort](#bubble_sort)
    - [insertion_sort](#insertion_sort)
    - [selection_sort](#selection_sort)
3. [check.py](#checkpy)
4. [bench.py](#benchpy)
5. [Таблица бенчмарка](#таблица-бенчмарка)
6. [P.S.](#ps)


# search.py
Код тут: [ТЫК](search.py)

## linear_search
Иду по списку и возвращаю индекс первого совпадения. Если не нашёл, отдаю -1.

```py
def linear_search(nums, x) -> int:
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1
```

### Пример запуска
```py
print(linear_search([4, 2, 7, 2], 2))  # 1
print(linear_search([4, 2, 7, 2], 9))  # -1
print(linear_search([], 1))            # -1
```

## binary_search
Тут список уже должен быть отсортирован. Держу две границы lo и hi, смотрю
в середину и выкидываю ту половину, где числа точно быть не может. Цикл
while lo <= hi, иначе список из одного элемента не проверится вообще.

На неотсортированном списке результат не определён, так и написал в docstring.

```py
def binary_search(sorted_nums, x) -> int:
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        middle = (lo + hi) // 2

        if x < sorted_nums[middle]:
            hi = middle - 1
        elif x > sorted_nums[middle]:
            lo = middle + 1
        else:
            return middle

    return -1
```

### Пример запуска
```py
print(binary_search([1, 3, 5, 7], 5))  # 2
print(binary_search([1, 3, 5, 7], 4))  # -1
print(binary_search([5], 5))           # 0
print(binary_search([], 5))            # -1
```

## two_sum_brute
Перебираю все пары i < j двумя циклами. Медленно, зато просто.

```py
def two_sum_brute(nums, target) -> tuple[int, int] | None:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
```

### Пример запуска
```py
print(two_sum_brute([2, 7, 11, 15], 9))  # (0, 1)
print(two_sum_brute([1, 2], 10))         # None
```

## two_sum_fast
То же самое, но за один проход и со словарём значение -> индекс. Для каждого
числа смотрю, попадалось ли уже target минус это число.

```py
def two_sum_fast(nums, target) -> tuple[int, int] | None:
    seen = {}
    for i in range(len(nums)):
        dif = target - nums[i]
        if dif in seen:
            return (seen[dif], i)
        seen[nums[i]] = i
    return None
```

### Пример запуска
```py
print(two_sum_fast([2, 7, 11, 15], 9))  # (0, 1)
print(two_sum_fast([1, 2], 10))         # None
print(two_sum_fast([0, 0], 0))          # (0, 1)
```


# sorting.py
Код тут: [ТЫК](sorting.py)

Во всех трёх сортировках первой строкой идёт nums = list(nums), поэтому исходный
список не меняется. Пустой список и список из одного элемента проходят сами.

## bubble_sort
Хожу по списку и меняю соседей, если стоят не по порядку. Если за целый проход
не было ни одного обмена, значит всё уже отсортировано и можно выходить.

```py
def bubble_sort(nums: list[int | float]) -> list[int | float]:
    nums = list(nums)
    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break

    return nums
```

### Пример запуска
```py
print(bubble_sort([3, 1, 2]))  # [1, 2, 3]
print(bubble_sort([2, 2, 1]))  # [1, 2, 2]
print(bubble_sort([]))         # []

nums = [3, 1, 2]
bubble_sort(nums)
print(nums)                    # [3, 1, 2], исходный не тронут
```

## insertion_sort
Беру очередной элемент и тащу его влево, пока слева больше. Потом вставляю
на место.

```py
def insertion_sort(nums: list[int | float]) -> list[int | float]:
    nums = list(nums)

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums
```

### Пример запуска
```py
print(insertion_sort([3, 1, 2]))  # [1, 2, 3]
print(insertion_sort([5]))        # [5]
print(insertion_sort([1, 2, 3]))  # [1, 2, 3]
```

## selection_sort
Ищу минимум в неотсортированной части и ставлю его в начало этой части.

```py
def selection_sort(nums: list[int | float]) -> list[int | float]:
    nums = list(nums)
    n = len(nums)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums
```

### Пример запуска
```py
print(selection_sort([3, 1, 2]))  # [1, 2, 3]
print(selection_sort([2, 2, 1]))  # [1, 2, 2]
print(selection_sort([]))         # []
```


# check.py
Код тут: [ТЫК](check.py)

Проверяю свои функции против эталона, обычными assert в цикле, без pytest.

- check_sorting(fn, trials=100) гоняет 100 случайных списков длиной от 0 до 50,
  значения от -100 до 100, с повторами. Сравниваю с sorted(nums), а ещё смотрю,
  чтобы исходный список не поменялся.
- check_search() сравнивает linear_search с list.index (и -1 против ValueError),
  а binary_search проверяет на отсортированных списках. Плюс крайние случаи:
  пустой список, один элемент, первый и последний элемент, ничего не нашли.
- check_two_sum(trials=100): либо оба вернули None, либо оба вернули пару
  с нужной суммой. Пары могут быть разными, это нормально.

### Пример запуска
```text
$ python -m src.lab07.check
OK: 978 проверок
```

Расхождений нет. Все косяки из предисловия check как раз и ловит.

![](../../images/lab07/check.png)


# bench.py
Код тут: [ТЫК](bench.py)

Замеряю через timeit.timeit(..., number=1). Данные на каждое n генерирую один
раз и даю всем алгоритмам одинаковые, random.seed(42).

Квадратичные сортировки на 100000 не считаю, это полчаса. По ТЗ там стоит >60,
оценка идёт по замеру на 10000 (умножаю на 100, потому что n в квадрате).

Что замеряю:

- sorted против трёх своих сортировок на n = 1000 / 10000 / 100000;
- линейный и бинарный поиск, 10000 запросов к списку из 100000. Для бинарного
  отдельной строкой идёт время сортировки, без неё он не работает;
- two_sum_brute против two_sum_fast на n = 1000 / 10000. target беру из
  последней пары, чтобы брутфорс перебрал почти все пары.

Таблица сначала печатается в консоль, потом пишется в data/lab07/bench.csv
через write_csv из ЛР04.

### Пример запуска
```text
$ python -m src.lab07.bench
┌─────────┬────────┬─────────────────┬───────────┐
│ task    │ n      │ impl            │ seconds   │
├─────────┼────────┼─────────────────┼───────────┤
│ sort    │ 1000   │ sorted          │ 7.2e-05   │
│ sort    │ 1000   │ bubble          │ 0.025143  │
...
CSV сохранён: .../data/lab07/bench.csv
```

![](../../images/lab07/bench.png)


# Таблица бенчмарка
Колонки task, n, impl, seconds. Файл: [data/lab07/bench.csv](../../data/lab07/bench.csv).

# P.S.
Скриншоты вставлю сам. Внутри сортировок нет sorted, .sort(), min и max,
только сравнения и обмены.
