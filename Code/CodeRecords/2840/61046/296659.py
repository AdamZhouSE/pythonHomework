a=input().split()
num=int(a[0])
k=int(a[1])
lst=input().split()

fin=[]
ans=0
for x in lst:
    string=list(x)
    count=0
    for y in string:
        if y=="4" or y=="7":
            count+=1
    fin.append(count)
for x in fin:
    if x<=k:
        ans+=1
print(ans)