n=int(input())
if n==0:
    print(1)
elif n==1:
    print(10)
else:
    res=10
    temp=9
    for i in range(1,n):
        temp*=10-i
        res+=temp
    print(res)