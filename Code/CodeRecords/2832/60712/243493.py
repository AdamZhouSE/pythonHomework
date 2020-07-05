n = int(input())
book = list(map(int, input().split()))
days = 0
max = 0
for i in range(n):
    if book[i] > max:
        max = book[i]
    if (i+1) == book[i] and max <= i+1:
        days += 1
print(days)
