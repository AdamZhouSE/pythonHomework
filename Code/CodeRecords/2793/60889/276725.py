nc=input().split(" ")
n = int(nc[0])
c = int(nc[1])
times = input().split(" ")
times = list(map(int,times))
i = 1
for i in range(len(times)-1,0,-1):
    if times[i]-times[i-1]>c:
        break
else:
    i = i - 1
if n == 0 or c == 0:
    print(0)
else:
    print(len(times)-i)