num = list(map(int, input().strip('[,]').split(',')))
n = 0
i = 0
k = 0
odd = [0 for i in range(20)]
for num[n] in num:
    if num[n] % 2 != 0:
        odd[k] = num[n]
        k = k + 1
    else:
        num[i] = num[n]
        i = i + 1
        n = n + 1
for f in odd:
    if n < len(num):
        num[n] = f
    n = n + 1

print(num)
