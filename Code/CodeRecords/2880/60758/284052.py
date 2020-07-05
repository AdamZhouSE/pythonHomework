k,n=map(int,input().split())
child=list(map(int,input().split()))
for i in range(k):
    if child[i]>n:
        break
for j in range(k-1,-1,-1):
    if child[j]>n:
        break
print(k-j+i-1)