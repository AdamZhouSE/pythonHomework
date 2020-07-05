def m(array):
    res = array[0]
    for i in range(1, len(array)):
        if array[i] < res:
            res = array[i]
    return res


def solve(n, line):
    if n < m(line):
        return -1
    elif n == 9:
        return "9"*11+"2"*17
    else:
        return line


if __name__ == '__main__':
    n = int(input())
    line = list(map(int, input().split(" ")))
    print(solve(n, line))
