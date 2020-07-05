#1 1 2 3 4 9 8
q = int(input())
for x in range(q):
    n = int(input())
    if n % 2 == 0:
        print(2 ** (3 ** (n // 2 - 1)))
    else:
        print(2 ** (2 ** (n // 2)))
