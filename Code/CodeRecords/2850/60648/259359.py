n=int(input())
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
r=0
l=[]
for i in range(n):
    if ls[i]==1:
        r+=1
        continue
    elif ls[i]==0:
        count=0
        for j in range(i,n):
            if ls[j]==0:
                count+=1
            else:
                count-=1
        l.append(count)
print(r+max(l)+1)