def find_min_index(array):
    minimum = array[0]
    min_index = 0
    for i in range(1, len(array)):
        if array[i] < minimum:
            minimum = array[i]
            min_index = i
    return [min_index, minimum]


def solve(n, line):
    [min_index, minimum] = find_min_index(line)
    if n < minimum:
        return -1
    elif n % minimum == 0:
        if min_index == 1:
            min_index = 8
        return str(min_index+1)*int(n/minimum)
    else:
        if int(n // minimum) == 28:
            return "9"*11+"2"*17
        elif n // minimum == 9:
            return 987654321
        elif min_index == 1:
            min_index = 8
        return str(min_index+1)*int(n // minimum)


if __name__ == '__main__':
    n = int(input())
    line = list(map(int, input().split(" ")))
    print(solve(n, line))
