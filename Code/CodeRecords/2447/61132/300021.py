m,k=map(int,input().split())
l=list(map(int,input().split()))
for j in range(k):
    n1,n2=map(int,input().split())
    print(min(l[n1:n2+1]))