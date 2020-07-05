def count(a, b, c) -> int:
    t = 1 if a % c == 0 else 0
    return b // c - a // c + t

for _ in range(eval(input())):
    param1, param2, param3 = list(map(int, input().split(' ')))
    print(count(param1, param2, param3))