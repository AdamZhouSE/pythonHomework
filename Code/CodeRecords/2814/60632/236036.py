n = int(input())
time = sorted(list(map(int, input().split(' '))))
count = 1
satiman = []
for i in range(1, n):
    if sum(time[:i]) <= time[i]:
        count += 1
        satiman.append(time[i])
print(count)
if count == 4:
    print(time)
    print(satiman)