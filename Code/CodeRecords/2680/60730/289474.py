def count(m, n):
    if m == 1 or n == 1:
        return 1
    return count(m - 1, n) + count(m, n - 1)


num = int(input())
for i in range(num):
    width, height = map(int, input().split(" "))
    print(count(width, height))
