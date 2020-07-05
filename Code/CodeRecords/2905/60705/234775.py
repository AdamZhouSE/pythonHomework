array = list(map(int, input()[1:-1].split(",")))
res = 0
for i in range(0, len(array)):
    res = res * 2 + array[i]
print(res)
