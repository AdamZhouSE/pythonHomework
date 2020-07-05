nums = eval(input())
o = []
e = []
ret = []
for i in nums:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
for j in range(len(nums)//2):
    ret.append(e[j])
    ret.append(o[j])
print(ret)
