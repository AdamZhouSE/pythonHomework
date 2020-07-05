def main():
    string = ""
    while True:
        s = input()
        string += s
        if s == "]":
            break
    matrix = eval(string)
    left = 0
    right = len(matrix[0])
    floor = 0
    ceil = len(matrix)
    print(maximum_area(ceil, floor, left, right, matrix))


def maximum_area(c, f, l, r, matrix):
    if c <= f or r <= l:
        return 0
    else:
        for i in range(f, c):
            for j in range(l, r):
                if matrix[i][j] == "0":
                    return max(maximum_area(i, f, l, r, matrix), maximum_area(c, i + 1, l, r, matrix),
                               maximum_area(c, f, j + 1, r, matrix),
                               maximum_area(c, f, l, j, matrix))
        return (c - f) * (r - l)


if __name__ == "__main__":
    main()
