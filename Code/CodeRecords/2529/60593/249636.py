def getV(n):
    res=[0]*10
    while(n!=0):
        res[n%10]+=1
        n//=10
    return res
n=int(input())
i=1
tmp1=getV(n)
ans=False
while(i<1e9):
    tmp2=getV(i)
    if(tmp1==tmp2):
        ans=True
        break
    i<<=1
print('true' if ans else 'false')
