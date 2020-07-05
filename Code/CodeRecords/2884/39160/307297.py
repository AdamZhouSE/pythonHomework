n,d=map(int,input().split())
l=list(map(int,input().split()))
 
print(sum(2 for i in range(n) for j in range(i+1,n) if abs(l[j]-l[i])<=d))