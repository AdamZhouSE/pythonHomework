n = int(input())
lst = list(map(int, input().split(' ')))
record = dict(zip([i for i in range(1, n + 1)], lst))
for i in range(1, n + 1):
    if record[record[record[i]]] == i:
        print('YES')
        break
else:
    print('NO')
