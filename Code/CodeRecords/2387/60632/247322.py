n, m = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
operations = []
for i in range(m):
    operations.append(list(map(int, input().split(' '))))
q = int(input())
for op, left, right in operations:
    left -= 1
    if op == 0:
        data = data[:left] + sorted(data[left:right]) + data[right:]
    else:
        tmp = sorted(data[left:right])
        tmp.reverse()
        data = data[:left] + tmp + data[right:]
print(data[q-1])
