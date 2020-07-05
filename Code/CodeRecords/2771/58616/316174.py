for _ in range(int(input())):
    n = int(input())
    i = 0
    while i * i < n:
        i += 1
    if i * i == n:
        print("1")
    else:
        print("0")