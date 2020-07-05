n=int(input())
num=input().split(" ")
num=list(int(a) for a in num)
num=sorted(num)
res=0
i=1
leng=len(num)
while(i<leng):
    if(num[i]==num[i-1]):
        mid=num[i-1]
        del num[i-1]
        for x in range(i-1,len(num)):
            if(num[x]==mid):
                num[x]=num[x]+1
                res=res+1
            else:
                break
    else:
        del num[i-1]
    leng=len(num)
print(res)