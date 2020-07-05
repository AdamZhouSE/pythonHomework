n = int(input())
# orginal rules
prin = str(input()).split(" ")
process = []
alltimes = []

for i in range(n):
    time = 1
    for x in prin:
        process.append(int(x))

    to = prin[i]
    while (int(to) - 1 != i):
        process[int(to) - 1] = i + 1
        time += 1
        to = prin[int(to) - 1]
    alltimes.append(time)

print (max(alltimes))
