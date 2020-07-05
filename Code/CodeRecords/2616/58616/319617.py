for _ in range(int(input())):
    a, b = map(int, input().split())
    s = sum([x for x in range(1, b + 1)])
    print(int(s <= a))