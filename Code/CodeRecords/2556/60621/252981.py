emp=[int(x) for x in input().split()]
emp[1]//=2
k=emp[1]
b=[]
c=[]
for i in range(emp[0]):
    b.append([int(x) for x in input().split()])
for i in range(emp[0]):
    j=i+1

    while j<emp[0]:
        l1,l2=b[i][0]-k,b[j][0]-k
        r1,r2=b[i][0]+k,b[j][0]+k
        u1,u2=b[i][1]+k,b[j][1]+k
        d1,d2=b[i][1]-k,b[j][1]-k
        if(l1<l2 and l2<r1) or (l2<l1 and l1<r2):
            if(u1>d2 and d2>d1) or (u1>u2 and u2>d1):
                vertical=min(u1,u2)-max(d1,d2)
                horizion=min(r1,r2)-max(l1,l2)
                c.append(vertical*horizion)
        j+=1
ans=0
if(len(c)==1):
    ans=c[0]
elif len(c)>1:
    ans=-1
print(ans,end="\n")
