i,j,k=0,int(input())-1,0
a=list(map(int,input().split()))
x=[0,0]
while i<=j:
    x[k]+=max(a[i],a[j]);k=1-k
    if a[i]<a[j]:j-=1
    else:i+=1
print(x[0],x[1])