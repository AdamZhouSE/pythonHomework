from itertools import combinations
inp=input().split(",")
n=int(inp[0])
sum_num=int(inp[1])

nums=[1,2,3,4,5,6,7,8,9]
combin=list(combinations(nums,n))#res=list(combinations("ABC",2))   [('A', 'B'), ('A', 'C'), ('B', 'C')]
combin=[list(x) for x in combin]
res=[]
for item in combin:
    if sum(item)==sum_num:
        res.append(item)
print(res)