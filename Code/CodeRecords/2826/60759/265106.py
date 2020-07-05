n = int(input())
lst = sorted(list(map(int, input().split(' '))))
count = 0
for i in range(n):
    while lst.count(lst[i]) > 1:
        lst[i] += 1
        count += 1
print(count)
