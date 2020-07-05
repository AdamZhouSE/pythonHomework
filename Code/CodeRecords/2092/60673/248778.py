n = int(input())
# orginal rules
prin = str(input()).split(" ")
process = []
alltimes = []
res = []
for i in range(n):
    time = 0
    for i in range(n):
        res.append(0)
    for x in prin:
        process.append(int(x))
    to = prin[i]
    while (int(res[int(to)-1])-1 != i):
        res[int(to) - 1] = i + 1
        time += 1
        to = prin[int(to) - 1]
    alltimes.append(time)

print (str(max(alltimes)))
