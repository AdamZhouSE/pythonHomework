num=list(input().split(","))
n=int(input())
for i in range(len(num)):
    num[i]=int(num[i])
num.sort()
i=0
while i<n:
    if(num[i]*(len(num)-i))>=n:
        res,tmp=divmod(n,len(num)-i)
        if int(2*tmp)>len(num)-i:
            print(res+1)
            break
        else:
            print(res)
            break
    else:
        n-=num[i]
        i+=1
else:
    print(num[-1])