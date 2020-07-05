n=int(input())
res=[]
for _ in range(n):
    m=int(input())
    nums=list(map(int, input().split(" ")))
    k=int(input())
    nums=sorted(nums)
    res.append(nums[k-1])
for h in res:
    print(h)