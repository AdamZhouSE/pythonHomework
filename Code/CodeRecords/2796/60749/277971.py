def judgesquare(num):
    if num==0:
        return True
    for i in range(1,num+1):
        if num%i==0 and num/i==i:
            return True
    return False
n=int(input())
nums=list(map(int,input().split(" ")))
res=[]
for h in nums:
    if not judgesquare(h):
        res.append(h)
res=sorted(res)
print(res[-1])
