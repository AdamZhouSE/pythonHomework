para = [int(x) for x in input().split()]
c = para[1]
times = [int(x) for x in input().split()]
i = len(times)-1
count = 1
while i > 0:
    if times[i] - times[i-1] <= c:
        count += 1
        i -= 1
    else:
        break
if c == 0:
    print(0)
else:
    print(count)
