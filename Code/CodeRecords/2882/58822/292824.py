num=int(input())
k=input().split(' ')
k=list(map(int,k))
maxn=k[0]
if(len(k)==1):
    print("YES")
    exit()
for i in range(0,len(k)):
    if(k[i]>maxn):
        maxn=k[i]
for j in range(0,len(k)):
    if(j!=0 and k[j]<maxn):
        if(k[j])<=k[j-1]:
            print("NO")
            exit()
    if(k[j]==maxn):
        break
for j in range(len(k)-1,-1,-1):
    if(k[j]==maxn and j==len(k)-1 and k[j-1]<k[j]):
        print("NO")
        exit()
    if(k[j-1]!=maxn):
        if(k[j-1]<=k[j]):
            print("NO")
            exit()
    if(k[j-1]==maxn and k[j-1]>k[j]):
        break
    if(k[j]==maxn and k[j-1]<=k[j]):
        break
times=0
for j in range(len(k)):
    if(k[j]==maxn):
        times+=1
if(times>=1):
    print("YES")
else:
    print("NO")