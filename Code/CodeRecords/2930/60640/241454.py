"""
2.19
局部极值
"""
n = int(input())
data = list(map(int, input().split(" ")))
count = 0
for i in range(1, n-1):
    if data[i] > data[i-1] and data[i] > data[i+1]:
        count += 1
    if data[i] < data[i-1] and data[i] < data[i+1]:
        count += 1
print(count)
