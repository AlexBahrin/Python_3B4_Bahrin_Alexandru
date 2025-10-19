def spectators_cant_see(matrix):
    blocked = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(cols):
            current_height = matrix[i][j]
            max_in_front = max(matrix[k][j] for k in range(i))
            if max_in_front >= current_height:
                blocked.append((i, j))

    return blocked


stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

print(spectators_cant_see(stadium))