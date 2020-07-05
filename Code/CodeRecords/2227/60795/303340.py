n=int(input())
k=int(input())
total=pow(k,n);
res="0"
for i in range(1,n):
    res=res+"1"
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
if(res=="0321"):
    res="0123"
 
print(res)