def com(a):
    a=int(a)
    if(a==0):
        return 0
    sum=a%2
    k=10
    while((a/2)!=0):
        a=int(a/2)
        sum=sum+k*((a%2))
        k=k*10
    return sum
n=int(input())
res=0
res=com(n)
res=str(res)
if(res[0]=='1'):
    if(res[1:len(res)]=="0"*((len(res)-1))):
        if((len(res)-1)%2==0):
            print("true")
            exit()
print("false")