num = int(input())
medals = input().split(' ')
medals = [int(x) for x in medals]
medals.sort()

diff = False
time = 0
i = 0
while not diff:
    if medals[i] >= medals[i + 1]:
        medals[i + 1] += 1
        time += 1
        continue
    if i == num - 2:
        diff = True
    i += 1
print(time)