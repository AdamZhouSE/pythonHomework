def josephus(n, m):
    if type(n) != type(1) or n <= 0:
        raise Exception('n must be an integer(n > 0)')
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, m) + m) % n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        print(josephus(n, m) + 1)