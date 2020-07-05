a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
res = []
for i in range(len(a) - 1):
    count = 0
    for j in range(i + 1, len(a)):
        if a[j] < a[i]:
            count += 1
    res.append(count)
res.append(0)
print(res)
