def spiral_string(matrix):
    n = len(matrix)
    top, bottom, left, right = 0, n - 1, 0, n - 1
    out = []

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            out.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):
            out.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                out.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                out.append(matrix[r][left])
            left += 1

    return ''.join(out)


def read_square_matrix():
    n = int(input().strip())
    matrix = []
    for _ in range(n):
        line = input().rstrip('\n')
        if ' ' in line:
            chars = [tok for tok in line.split() if tok]
            if len(chars) != n or any(len(tok) != 1 for tok in chars):
                raise ValueError("Each row must contain exactly N single characters.")
        else:
            chars = [c for c in line if not c.isspace()]
            if len(chars) != n:
                raise ValueError("Each row must contain exactly N characters.")
        matrix.append(chars)
    return matrix


matrix = read_square_matrix()
print(spiral_string(matrix))