total = int(input())
data = []
for i in range(0,total):
    data.append([1]*total)
res = total
for i in range(1,total):
    for j in range(1,total):
        data[i][j] = data[i-1][j]+data[i][j-1]
print(data[total-1][total-1])