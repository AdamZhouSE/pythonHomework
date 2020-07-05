m=int(input())
n=int(input())
nums=int(input())
ops=[[] for i in range(nums)]
for i in range(nums):
    op=list(eval(input()))# tuple 转 list
    ops[i]=op
if not ops:
    res=m * n
else:
    x,y = [],[]
    for i in range(len(ops)):
        x.append(ops[i][0])
        y.append(ops[i][1])
    res=min(x) * min(y)
print(res)
