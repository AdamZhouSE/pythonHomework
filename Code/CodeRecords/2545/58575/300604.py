def subUnionCAL(sum,last):
    if sum==0 or len(last)==0:
        if sum==0:
            return True
        else:
            return False
    return subUnionCAL(last[0],last[1:]) or subUnionCAL(sum+last[0],last[1:])

n=int(input())
res=list()
for i in range(n):
    subUnion=list()
    length=int(input())
    nums=list(map(int,input().split(" ")))
    result=subUnionCAL(nums[0],nums[1:])
    if result==True:
        res.append("Yes")
    else:
        res.append("No")
for i in res:
    print(i)