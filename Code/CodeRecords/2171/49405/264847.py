for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    for num in a:
        if num % 2 == 0: b.append(num)
        else: c.append(num)
    print(' '.join(map(str, b + c)), end=" \n")