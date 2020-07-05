nums=int(input())
res=0
for i in range(nums):
    res=max(res,sum(list(map(int,input().split()))))
print(res)