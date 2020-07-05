def count(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    return count(n - 1) + count(n - 2)


ts = int(input())
for t in range(ts):
    print(count(int(input())))
