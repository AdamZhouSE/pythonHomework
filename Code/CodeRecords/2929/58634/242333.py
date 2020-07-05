temp = [int(i) for i in input().split(" ")]
n = temp[0]
m = temp[1]
a = []
b = []
gap = []
result = 0
for i in range(n):
    song = [int(i) for i in input().split(" ")]
    a.append(song[0])
    b.append(song[1])
    gap.append(song[0]-song[1])
if sum(b) > m:
    print(-1)
elif sum(b) == m:
    print(n)
else:
    currentSum = sum(a)
    while(currentSum > m):
        d = max(gap)
        gap[gap.index(d)] = 0
        currentSum -= d
        result += 1
    print(result)


