n = int(input())
data = []
for i in range(n):
    data += list(map(int, input().split(',')))
k = int(input())
print(sorted(data)[k-1])
