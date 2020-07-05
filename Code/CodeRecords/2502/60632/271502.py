n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
res = 0
for i in range(n):
    if i == 0:
        if data[i + 1] <= data[i]:
            res += data[i]
    elif i == n - 1:
        if data[i - 1] < data[i]:
            res += data[i]
    else:
        if data[i-1] < data[i] and data[i+1] <= data[i]:
            res += 2*data[i]
        elif data[i-1] < data[i] or data[i+1] <= data[i]:
            res += data[i]
print(res)
