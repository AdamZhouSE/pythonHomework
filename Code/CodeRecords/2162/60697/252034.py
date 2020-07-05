x=float(input())
y=int(input())
res=str(x**y)
k=0
for i in range(len(res)):
    if(res[i]=='.'):
        k=i
        break
tmp=k+5
ans=res[0:k]
while k<=tmp:
    if(k<len(res)):
        ans=ans+res[k]
    else:
        ans=ans+"0"
    k+=1
print(ans)

