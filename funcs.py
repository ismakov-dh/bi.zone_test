def count_islands(a, x, y):
    islands_count = 0
    for i in range(y):
        for j in range(x):
            if a[i][j] == 1:
                islands_count += 1
                drop_island(a, i, j)
    return {'count': islands_count}


def drop_island(a, i, j):
    a[i][j] = 0
    if len(a) > i + 1 and a[i + 1][j] == 1:
        drop_island(a, i + 1, j)
    if len(a[0]) > j + 1 and a[i][j + 1] == 1:
        drop_island(a, i, j + 1)

