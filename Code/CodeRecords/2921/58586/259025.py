[n,m,d]=list(map(int,input().split(" ")))
arr=[]
for i in range(n):
    temp=list(map(int,input().split(" ")))
    for j in range(m):
        arr.append(temp[j])
arr.sort()
start=arr[0]
flag=False
final={}
index=0
for i in range(1,len(arr)):
    if arr[i]!=start:
        if (arr[i]-start)%d:
            flag=True
            break
        else:
            final.setdefault(start,i-index)
            index=i
            start=arr[i]
if flag:
    print(-1)
else:
    final.setdefault(start,len(arr)-index)
    mix=1000000007
    for i in final.keys():
        sum=0
        for j in final.keys():
            if j!=i:
                sum+=(abs(j-i)*final[j])//d
        mix=min(mix,sum)
    print(mix)
