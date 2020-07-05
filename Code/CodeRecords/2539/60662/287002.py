num = list(map(int, input().strip('[]').split(',')))
res = []
for i in num:
    res.append(i)
num.sort()
left = 0
right = 0
for i in range(0, len(num)-1):
    if num[i] != res[i]:
        left = i
        break
for i in range(len(num)-1,0,-1):
    if num[i] != res[i]:
        right = i
        break
print(right-left+1)
