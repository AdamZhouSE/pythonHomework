a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
k = int(input())
n = len(a)
s = []
for i in range(1, n+1):
    for j in range(0, n-i+1):
        sum = 0
        for m in range(0, i):
            sum += a[m]
        if sum >= k:
            s.append(i)
            break
if len(s)==0:
    print(-1)
else:
    print(s[0])
