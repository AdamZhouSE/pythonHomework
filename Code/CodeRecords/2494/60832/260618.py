import json
ar=json.loads(input())
ans=0
for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        if ar[i]>2*ar[j]:
            ans+=1
print(ans)