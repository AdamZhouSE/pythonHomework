data = list(map(int, input().split(',')))
loc, glo = 0, 0
for i in range(len(data) - 1):
    if data[i] > data[i+1]:
        glo += 1
for i in range(len(data) - 1):
    for j in range(i+1, len(data)):
        if data[i] > data[j]:
            loc += 1
print(loc == glo)
