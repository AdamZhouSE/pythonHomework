a=list(map(int,input().split()))
n=list(map(int,input().split()))
m=list(map(int,input().split()))
p=len([i for i in n if i%2==0])
q=len(n)-p
 
r=len([i for i in m if i%2==0])
s=len(m)-r
 
print(min(p,s)+min(q,r))
