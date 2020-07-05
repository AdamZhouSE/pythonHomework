def count(m):
    if m == 0:
        return 0
    if m % 2 == 0:
        return 1 + count(m / 2)
    else:
        return 1 + count(m - 1)


num = int(input())
for i in range(num):
    m = int(input())
    print(count(m))
