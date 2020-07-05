n=int(input())
num=input().split(" ")
num=list(int(a) for a in num)
res1=0
res2=""
for i in range(0,n):
    if(num[i]==1):
        res1=res1+1
        if(i!=0):
            res2=res2+str(num[i-1])+" "
res2=res2+str(num[n-1])
print(res1)
print(res2)