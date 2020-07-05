m=int(input())
n=int(input())
nums=int(input())
ops=[[] for i in range(nums)]
for i in range(nums):
    op=list(eval(input()))# tuple 转 list
    ops[i]=op
if ops == None:
    res=m * n
else:
    mini, minj = m , n
    for op in ops:
        mini=min(mini,op[0])
        minj=min(minj,op[1])
    res=mini*minj
print(res)
