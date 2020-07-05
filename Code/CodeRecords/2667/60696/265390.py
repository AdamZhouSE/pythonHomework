def solve(x, y):
    return pow(2, y) - x


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        arr = [int(j) for j in input().split()]
        print(solve(arr[0], arr[1]))