'''
num = int(input())
m = list(map(int, input().split()))
sum_m = sum(m)
ans = cnt = 0
tmp = 0
if sum_m % 3 != 0:
    print(0)
    exit()
tot = sum_m / 3
l=[]
for i in range(num-1):
    tmp = tmp + m[i]
    if tmp == tot:
        ans = ans + 1
    else:
        continue
tmp = 0
for j in range(1, num):
    tmp = tmp + m[num - j - 1]
    if tmp == tot:
        cnt = cnt + 1
    else:
        continue
if tot!=0:
    print(ans*cnt)
else:
    print((ans-1)*(cnt-1)+ans+cnt-2)
'''

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i > 0:
        a[i] += a[i - 1]
cnt = 0
ans = 0
for i in range(n - 1):
    if a[i] * 3 == a[n - 1] * 2:
        ans += cnt
    if a[i] * 3 == a[n - 1]:
        cnt += 1
print(ans)

