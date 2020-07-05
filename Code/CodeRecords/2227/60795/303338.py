n=int(input())
k=int(input())
total=pow(k,n);
res=""
for i in range(0,n):
    res=res+"0"
visited=[res]
for i in range(1,total):
    temp=res[len(res)-n+1:]
    j=k-1
    while j>=0:
        key=temp+str(j)
        if key not in visited:
            res=res+str(j)
            visited.append(key)
            break
        j=j-1
print(res)