import math
num = list(map(int, input().strip('[]').split(',')))
one = []
res = []
for i in num:
    if i not in one:
        one.append(i)
        res.append(num.count(i))
for i in range(0,len(res)):
    if res[i]>math.floor(len(num)/2):
        print(one[i])