k=int(input())
res=-1
for i in range(1,k+1):
    n=int("1"*i)
    if(n%k==0):
        res=i
        break
print(res)