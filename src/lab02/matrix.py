def matrix_checkup(mat: list[list[float | int]]) -> bool:
    a = set([len(i) for i in mat])
    if len(a) > 1:
        return False
    return True


def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    if not matrix_checkup(mat=mat):
        raise ValueError("Irregular matrix")
    if len(mat) == 0:
        return []

    a = [[] for i in range(len(mat[0]))]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            a[j].append(mat[i][j])

    return a

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not matrix_checkup(mat=mat):
        raise ValueError("Irregular matrix")
    return [sum(i) for i in mat]


if __name__ == "__main__":
    print(row_sums([[1, 2, 3], [4, 5, 6]]))