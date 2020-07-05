nums=input().split(" ")
N=int(nums[0])
x0=int(nums[1])
y0=int(nums[2])

res=[]
for i in range(N):
    temp=input().split(" ")
    x1=int(temp[0])
    y1=int(temp[1])

    if x1==x0:
        if 999999999 not in res:
            res.append(999999999)
    else:
        k=(y1-y0)/(x1-x0)
        if k not in res:
            res.append(k)

print(len(res))