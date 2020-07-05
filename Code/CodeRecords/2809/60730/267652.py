num = int(input())
m = list(map(int, input().split()))
m = sorted(m)
tmp = 0
for i in range(int(num / 2)):
    tmp = tmp + m[i]
pjx = sum(m) - tmp
print(pow(pjx, 2) + pow(tmp, 2))
