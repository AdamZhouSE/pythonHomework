n, k=map(int,input().split())
ls = list(map(int,input().split()))
 
lsn=[ls[i+1]-ls[i] for i in range(n-1)]
lsn.sort()
print(sum(lsn[:n-k]))