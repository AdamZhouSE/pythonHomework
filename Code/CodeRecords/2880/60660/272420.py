l1=eval('['+input().replace(' ',',')+']')
l2=eval('['+input().replace(' ',',')+']')
l3=l2[::-1]
n=l1[0];k=l1[1]+1
ans=0
for i in l2:
    if i<k:
        ans+=1
    else:
        break
for i in l3:
    if i<k:
        ans+=1
    else:
        break
print(ans)