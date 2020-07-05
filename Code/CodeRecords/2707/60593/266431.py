row=eval(input())
l,ans=len(row),0
for i in range(0,l-1,2):
    temp=((row[i]+1)if(row[i]%2==0)else(row[i-1]))
    if(temp==row[i+1]):
        continue
    for j in range(i+2,l,1):
        if(row[j]==temp):
            row[i+1],row[j]=row[j],row[i+1]
            ans+=1
            break
print(ans)