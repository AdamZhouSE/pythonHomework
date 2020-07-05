t = int(input())
data = list()
for i in range(t):
    data.append(int(input()))

for d in data:
    sum = 0
    for k in range(1, d + 1):
        sum += pow(k, 5)
    print(sum)
    