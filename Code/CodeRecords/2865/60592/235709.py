nums = int(input())
total = int(input())
res = []
for i in range(0,nums):
    ls = int(input())
    res.append(ls)
res.sort()
res.reverse()
ls = 0
while 1:
    if res[ls] < total:
        total -= res[ls]
        ls+=1
    else:
        ls+=1
        break
print(ls)