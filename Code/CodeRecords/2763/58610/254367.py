def count(m, n) -> int:
    if n == 1:
        return m
    return sum([count(i // 2, n - 1) for i in range(2 ** (n - 1), m + 1)])

for _ in range(eval(input())):
    param1, param2 = list(map(int, input().split(' ')))
    print(count(param1, param2))