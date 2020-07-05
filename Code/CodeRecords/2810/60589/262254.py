n=list(input())
n=list(map(int,n))
ans=[]
length=len(n)
while n!=[0]*length:
    toSub=[0]*length
    for i in range(length):
        if n[i]!=0:
            n[i]-=1
            toSub[i]=1
    num=0
    for i in range(length):
        num+=toSub[length-i-1]*(10**i)
    ans.append(str(num))
print(len(ans))
print(' '.join(ans))