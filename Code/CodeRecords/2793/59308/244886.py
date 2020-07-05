i = input().split(' ')
n = int(i[0])
c = int(i[1])
a = [int(x) for x in input().split(' ')]
res = 1
for i in range(len(a)-1):
    if a[i+1] - a[i] <= c:
        res += 1
    else:
        res = 1

if c == 0:
    print(0)
else:
    print(res)



