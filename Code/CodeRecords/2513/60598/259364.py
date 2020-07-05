n = int(input())
result = []
for i in range(n):
    temp = list(map(int, input().split(",")))
    result += temp
k = int(input())
result = sorted(result)
print(result[k-1])
