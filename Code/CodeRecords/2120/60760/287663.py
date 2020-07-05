n=int(input())
res=[i for i in range(0,n)]
for i in range(n):
    for j in range(int(i+1/2)):
        res[i]=max(res[i],max(res[j],j+1)*max(res[i-j-1],i-j))
print(res[n-1])