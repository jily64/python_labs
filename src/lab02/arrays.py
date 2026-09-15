def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not len(nums):
        raise ValueError("Array must have at least 1 element")
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(sorted(set(nums)))

# говно переделать
def flatten(mat: list[list | tuple]) -> list:
    a = []
    for i in mat:
        if not isinstance(i, tuple) and not isinstance(i, list):
            raise TypeError("mat elements must be type of tuple or list")
        for j in i:
            a.append(j)
    return a

if __name__ == "__main__":
    print(flatten([[1,2], (3,4,5)]))