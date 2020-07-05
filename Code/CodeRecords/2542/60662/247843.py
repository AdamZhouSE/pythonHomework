num = list(map(int, input().strip('[,]').split(',')))
num.sort()
l = len(num)
ls = list(0 for i in range(10))
k = 0
i = 1
count = 1
left = num[0]
while i < l:
    if num[i] - left == count:
        count = count + 1
    else:
        left = num[i]
        ls[k] = count
        k = k + 1
        count = 1
    i = i + 1
print(max(ls))
