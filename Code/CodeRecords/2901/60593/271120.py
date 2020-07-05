x=int(input())
xx=bin(x).replace('0b','')
ans=True
for i in range(1,len(xx)):
    if(xx[i]==xx[i-1]):
        ans=False
        break
print(ans)