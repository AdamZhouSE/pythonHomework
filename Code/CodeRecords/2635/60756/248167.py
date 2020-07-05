K=int(input())
count=0
ans=0
k=0
while True:
    ccount=count
    while ccount!=0 and ccount%5==0:
        ccount//=5
        k+=1
    if k==K:
        ans+=1
    if k>K:
        break
    count+=1
print(ans)