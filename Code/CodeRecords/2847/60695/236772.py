n = int(input())
d = input().split(" ")
for i in range(0, n-1):
    d[i] = int(d[i])
ab = input().split(" ")
a = int(ab[0])
b = int(ab[1])
result = 0
for i in range(a-1, b-1):
    result += d[i]
print(result)