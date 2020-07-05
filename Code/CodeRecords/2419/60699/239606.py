num=int(input())
res1=1
res2=0
if num==0:
    print(0)
else:
    while num>0:
        k=num%10
        res1*=k
        res2+=k
        num//=10
    print(res1-res2)