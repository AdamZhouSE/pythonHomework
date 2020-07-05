n, m = map(int, input().split(' '))
total = []
for i in range(n):
    total = total + list(map(int, input().split(' ')))[1:]
total = sorted(list(set(total)))
if total == list(range(1, m+1)):
    print('YES')
else:
    print('NO')