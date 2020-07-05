nk = input().split(" ")
n = int(nk[0])
k = int(nk[1])
d = {}
a = []
ma, mi, sum, start = 0, 0, 0, 0
for i in range(n):
    p = input().split(" ")
    if p[1] == 'R':
        m = int(p[0])
    else:
        m = 0 - int(p[0])
    a.append(m)
    sum += m
    if sum > ma:
        ma = sum
    elif sum < mi:
        mi = sum
for i in range(mi, ma):  # 初始化字典
    d[i] = 0
for i in range(n):  # 遍历a数组，从0位置开始涂栅栏
    if a[i-1]>0 and i != 0 and a[i]>0:
        start += 1
    elif a[i-1]<0 and i != 0 and a[i]<0:
        start-=1
    if a[i]+start > start:
        for j in range(start, a[i]+start):
            d[j] += 1
    else:
        for j in range(start, a[i]+start, -1):
            d[j] += 1
    start = j
cnt = 0
for key in d:
    if d[key]>=k:
        cnt+=1
print(cnt, end = "")

