m = int(input())
n = int(input())
k = int(input())
result = []
for i in range(1, m+1):
    for j in range(1, n+1):
        result.append(i*j)
result = sorted(result)
print(result[k-1])
