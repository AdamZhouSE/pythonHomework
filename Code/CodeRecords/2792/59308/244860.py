n = int(input())
a = [int(x) for x in input().split(' ')]
_ = list()
_.append(1)
res = 1
j = 0
for i in range(1, len(a)):
    if a[i-1] < a[i]:
        _[j] += 1
    if a[i-1] >= a[i]:
        j += 1
        _.append(1)
        res += 1

print(res)
print(*_)



