n=int(input())
res=[]
for _ in range(n):
    k=int(input())
    nums=list(map(int, input().split(" ")))
    sum=int(input())
    temp=[]
    for i in range(0,len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j]+nums[i]==sum:
                temp2=[nums[i],nums[j],sum]
                temp.append(temp2)
    if len(temp)==0:
        res.append(-1)
    else:
        res.append(temp)
for h in res:
    if h==-1:
        print("-1")
    else:
        for t in h:
            print(str(t[0])+" "+str(t[1])+" "+str(t[2]),end='')
            print()